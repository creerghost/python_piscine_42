from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import StrEnum
from typing import Any, Self, List, Dict, Set
from datetime import datetime


class Rank(StrEnum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_mission_rules(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with M")
        ranks: Set[Rank] = {Rank.commander, Rank.captain}
        if not any(member.rank in ranks for member in self.crew):
            raise ValueError("Mission must have a commander or captain")
        if self.duration_days > 365:
            experienced_crew: List[CrewMember] = [
                member for member in self.crew if member.years_experience > 5
            ]
            if len(experienced_crew) / len(self.crew) < 0.5:
                raise ValueError("Long-duration missions require"
                                 " at least 50% experienced crew")
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 30)
    print("Valid mission created:")

    valid_crew: List[CrewMember] = [
        CrewMember(
            member_id="CM-001",
            name="Sarah Connor",
            rank=Rank.commander,
            age=45,
            specialization="Mission Command",
            years_experience=20,
            is_active=True
        ),
        CrewMember(
            member_id="CM-002",
            name="John Smith",
            rank=Rank.lieutenant,
            age=35,
            specialization="Navigation",
            years_experience=10,
            is_active=True
        ),
        CrewMember(
            member_id="CM-003",
            name="Alice Johnson",
            rank=Rank.officer,
            age=25,
            specialization="Engineering",
            years_experience=5,
            is_active=True
        )
    ]

    valid_mission: Dict[str, Any] = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": datetime.now(),
        "duration_days": 900,
        "crew": valid_crew,
        "mission_status": "planned",
        "budget_millions": 2500.0
    }

    try:
        mission = SpaceMission(**valid_mission)
        print(f"Mission Name: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions} M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank}) - {member.specialization}")
    except ValidationError as e:
        print(e.errors()[0]['ctx']['error'])

    print("\n" + "=" * 30)
    print("Expected validation error:")

    invalid_crew: List[CrewMember] = [
        CrewMember(
            member_id="CM-001",
            name="John Doe",
            rank=Rank.officer,
            age=25,
            specialization="Pilot",
            years_experience=2,
            is_active=True
        ),
        CrewMember(
            member_id="CM-002",
            name="Vladimir Nikolaev",
            rank=Rank.captain,
            age=25,
            specialization="Python Developer",
            years_experience=1,
            is_active=True
        )
    ]

    invalid_mission: Dict[str, Any] = {
        "mission_id": "M-2024-001",
        "mission_name": "Mars Mission",
        "destination": "Mars",
        "launch_date": datetime.now(),
        "duration_days": 390,
        "crew": invalid_crew,
        "mission_status": "planned",
        "budget_millions": 1000.0
    }

    try:
        mission = SpaceMission(**invalid_mission)
    except ValidationError as e:
        print(e.errors()[0]['ctx']['error'])


if __name__ == "__main__":
    main()
