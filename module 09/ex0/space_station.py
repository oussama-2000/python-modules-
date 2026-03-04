from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime

class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        test1 = SpaceStation(
            name = "International Space Station",
            station_id = "ISS001",
            crew_size = 6,
            power_level = 85.5,
            oxygen_level = 92.3,
            is_operational = True,
            last_maintenance = datetime.now(),

        )
        print("Valid station created:")
        print(
            f"ID: {test1.station_id}\n"
            f"Name: {test1.name}\n"
            f"Crew: {test1.crew_size} people\n"
            f"Power: {test1.power_level}%\n"
            f"Oxygen: {test1.oxygen_level}%\n"
            f"Status: {'Operational' if test1.is_operational else 'Offline'}"
        )
        print("\n========================================")
        test2 = SpaceStation(
            name = "oussDDD",
            station_id = "ddd",
            crew_size = 21,
            power_level = 10,
            oxygen_level = 10,
            is_operational = True,
            last_maintenance = "2004-12-11",

        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])

if __name__ == "__main__":
    main()

