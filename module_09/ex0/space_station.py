from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional, Dict, Any


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    data: Dict[str, Any] = {
        "station_id": "ISS154",
        "name": "International Space Station",
        "crew_size": 7,
        "power_level": 88.5,
        "oxygen_level": 94.2,
        "last_maintenance": "2023-11-15T00:00:00",
        "is_operational": True,
        "notes": "All systems nominal"
    }

    invalid_data: Dict[str, Any] = {
        "station_id": "ISS154",
        "name": "International Space Station",
        "crew_size": 50,
        "power_level": 88.5,
        "oxygen_level": 94.2,
        "last_maintenance": "2023-11-15T00:00:00",
        "is_operational": True,
        "notes": "All systems nominal"
    }
    try:
        station = SpaceStation(**data)
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(f"Status: {'Operational' if station.is_operational
                         else 'Down'}\n")

        print("=" * 40)
        print("Expected validation error:")
        station = SpaceStation(**invalid_data)
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
