
from datetime import datetime
try:
    from pydantic import (
        BaseModel, Field, ValidationError
    )
except ImportError:
    raise SystemExit(
        "Error: the 'pydantic' package is required but not installed.\n"
        "Install it with: pip install pydantic"
    )


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field()
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 7, 22, 12, 41),
            is_operational=True,
        )
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(
            f"Status: {'Operational' if station.is_operational else 'Offline'}"
        )
        print()
        print("=" * 40)
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])

    try:
        SpaceStation(
            station_id="ISS001",
            name="Error Station",
            crew_size=42,
            power_level=50.0,
            oxygen_level=42.0,
            last_maintenance=datetime(2026, 8, 14, 12, 0),
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
