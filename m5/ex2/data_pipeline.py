
from abc import abstractmethod, ABC
from typing import Any, Protocol


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.ingested: list[Any] = []
        self.ingested_count: int = 0
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        return True

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        outp = (self.rank, str(self.ingested[0]))
        self.rank += 1
        self.ingested.pop(0)
        return outp


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(element, (int, float)) for element in data)
        return False

    def ingest(self, data: int | float | list[int] | list[float]) -> None:
        if self.validate(data):
            if isinstance(data, int) or isinstance(data, float):
                self.ingested_count += 1
                self.ingested.append(str(data))
            elif isinstance(data, list):
                self.ingested_count += len(data)
                for element in data:
                    self.ingested.append(str(element))
        else:
            raise ValueError("Got exception: Improper numeric data")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(i, str) for i in data)
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data):
            if isinstance(data, str):
                self.ingested_count += 1
                self.ingested.append(data)
            elif isinstance(data, list):
                self.ingested_count += len(data)
                for element in data:
                    self.ingested.append(element)
        else:
            raise ValueError("Got exception: Improper textual data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(key, str) and isinstance(value, str)
                       for key, value in data.items())
        if isinstance(data, list):
            return all(self.validate(item) for item in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data):
            if isinstance(data, dict):
                self.ingested_count += 1
                self.ingested.append(f"{data['log_level']}: {data['log_message']}")  # noqa: E501
            elif isinstance(data, list):
                self.ingested_count += len(data)
                for d in data:
                    self.ingested.append(f"{d['log_level']}: {d['log_message']}")  # noqa: E501
        else:
            raise ValueError("Got exception: Improper log data")


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        output = ",".join([value for key, value in data])
        print(f"CSV Output:\n{output}")


class JSONExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = ", ".join(
            f'"item_{key}": "{value}"'
            for key, value in data
        )
        output = "{" + values + "}"
        print(f"JSON Output:\n{output}")


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if isinstance(proc, DataProcessor):
            self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            for processor in self.processors:
                if processor.validate(data):
                    processor.ingest(data)
                    break
            else:
                print(
                    "DataStream error - Can't process element in stream:"
                    f" {data}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
        else:
            for processor in self.processors:
                print(
                    f"{type(processor).__name__}: "
                    f"total {processor.ingested_count} items processed, "
                    f"remaining {len(processor.ingested)} on processor"
                )
        print()

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            data = []
            for _ in range(min(nb, len(processor.ingested))):
                data.append(processor.output())
            plugin.process_output(data)


def main() -> None:
    print("""=== Code Nexus - Data Pipeline ===

Initialize the Data Stream...
""")
    ds: DataStream = DataStream()
    ds.print_processors_stats()
    print("Registering Processors\n")
    np: NumericProcessor = NumericProcessor()
    tp: TextProcessor = TextProcessor()
    lp: LogProcessor = LogProcessor()
    ds.register_processor(np)
    ds.register_processor(tp)
    ds.register_processor(lp)
    data: list[Any] = ['Hello world', [3.14, -1, 2.71],
                       [{'log_level': 'WARNING',
                         'log_message': 'Telnet access! Use ssh instead'},
                        {'log_level': 'INFO',
                         'log_message': 'User wil is connected'}],
                       42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {data}\n")
    ds.process_stream(data)
    ds.print_processors_stats()
    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_ep = CSVExportPlugin()
    ds.output_pipeline(3, csv_ep)
    print()
    ds.print_processors_stats()
    new_data: list[Any] = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days',
            },
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello',
    ]
    print(f"Send another batch of data: {new_data}")
    ds.process_stream(new_data)
    ds.print_processors_stats()
    print("Send 5 processed data from each processor to a JSON plugin:")
    json_ep = JSONExportPlugin()
    ds.output_pipeline(5, json_ep)
    print()
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
