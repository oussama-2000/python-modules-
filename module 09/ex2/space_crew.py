from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime
from typing import List


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class SpaceMission(BaseModel):
    mission_id: str = Field(
        min_length=5,
        max_length=15,
        description="mission ID"
        )
    mission_name: str = Field(
        min_length=3,
        max_length=100,
        description="mission name"
        )
    destination: str = Field(
        min_length=3,
        max_length=50,
        description="mission destination"
        )
    launch_date: datetime
    duration_days: int = Field(
        ge=1,
        le=3560,
        description="mission duration days"
        )
    crew: List["CrewMember"] = Field(
        min_length=1,
        max_length=12,
        description="mission members"
        )
    mission_status: str = Field(
        default="planned",
        description="mission status"
        )
    budget_millions: float = Field(
        ge=1.0,
        le=10000.0,
        description="mission budget millions"
        )

    class CrewMember(BaseModel):
        member_id: str = Field(
            min_length=3,
            max_length=10,
            description="member ID"
            )
        name: str = Field(
            min_length=2,
            max_length=50,
            description="member name"
            )
        rank: Rank
        age: int = Field(
            ge=18,
            le=80,
            description="member age"
            )
        specialization: str = Field(
            min_length=3,
            max_length=30,
            description="member specialization"
            )
        years_experience: int = Field(
            ge=0,
            le=50,
            description="member experience"
            )
        is_active: bool = Field(
            default=True,
            description="if the member is active"
            )

    @model_validator(mode="after")
    def validator(self) -> "SpaceMission":
        ranks = [member.rank.value for member in self.crew]
        if Rank.commander.value not in ranks and Rank.captain.value not in ranks:
            raise ValueError("Must have at least one Commander or Captain")
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        for member in self.crew:
            if self.duration_days > 365 and\
                    not member.years_experience >= 5:
                raise ValueError("Long missions (> 365 days) need 50\%\ experienced crew (5+ years)")
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self


if __name__ == "__main__":
    try:
        print("Space Mission Crew Validation")
        print("=========================================")
        member_1 = SpaceMission.CrewMember(
            member_id="member1",
            name="Sarah Connor",
            rank="commander",
            age=20,
            specialization="Mission Command",
            years_experience=5,
            is_active=True
        )
        member_2 = SpaceMission.CrewMember(
            member_id="member1",
            name="John Smith",
            rank="lieutenant",
            age=20,
            specialization="Navigation",
            years_experience=5,
            is_active=True
        )
        member_3 = SpaceMission.CrewMember(
            member_id="member1",
            name="Sarah Connor",
            rank="officer",
            age=20,
            specialization="Engineering",
            years_experience=5,
            is_active=True
        )
        crews = [member_1, member_2, member_3]

        valid_mession = SpaceMission(
            mission_id="Mv2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            budget_millions=2500.0,
            crew=crews
        )
        print(
            "Valid mission created:\n"
            f"Mission: {valid_mession.mission_name}\n"
            f"ID: {valid_mession.mission_id}\n"
            f"Destination: {valid_mession.destination}\n"
            f"Duration: {valid_mession.duration_days} days\n"
            f"Budget: ${valid_mession.budget_millions}M\n"
            f"Crew size: {len(valid_mession.crew)}"
        )
        print("Crew members:")
        for member in valid_mession.crew:
            print(f"- {member.name} ({member.rank.value}) - {member.specialization}")
        print("\n=========================================")

    except ValidationError as e:
        print(f"Expected validation error:\n{e.errors()[0]['msg'][13:]}")