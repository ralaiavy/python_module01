
from abc import abstractmethod, ABC
from typing import Any


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


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    n = NumericProcessor()
    t = TextProcessor()
    l = LogProcessor()  # noqa: E741
    numbers: list[int] = [1, 2, 3, 4, 5]
    words: list[str] = ["Hello", "Nexus", "World"]
    logs: list[dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'},
    ]
    print(f"""Testing Numeric Processor...
Trying to validate input '42': {n.validate(42)}
Trying to validate input 'Hello': {n.validate("Hello")}
Test invalid ingestion of string 'foo' without prior validation:""")
    try:
        n.ingest("foo")
    except ValueError as e:
        print(e)
    print(f"""Processing data: {numbers}
Extracting 3 values...""")
    n.ingest(numbers)
    for _ in range(3):
        rank, value = n.output()
        print(f"Numeric value {rank}: {value}")
    print(f"""
Testing Text Processor...
Trying to validate input '42': {t.validate(42)}
Processing data: {words}
Extracting 1 value...""")
    t.ingest(words)
    t_rank, t_value = t.output()
    print(f"Text value {t_rank}: {t_value}")
    print(f"""
Testing Log Processor...
Trying to validate input 'Hello': {l.validate("Hello")}
Processing data: {logs}
Extracting 2 values...""")
    l.ingest(logs)
    for _ in range(2):
        l_rank, l_value = l.output()
        print(f"Log entry {l_rank}: {l_value}")


if __name__ == "__main__":
    main()
