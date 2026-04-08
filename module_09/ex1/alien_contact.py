from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import StrEnum
from datetime import datetime
from typing import Optional, Self, Any, Dict


class ContactType(StrEnum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=1, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=100)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def check_rules(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with AC")
        if (self.contact_type == ContactType.physical
                and not self.is_verified):
            raise ValueError("Physical contact must be verified")
        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError("Telepathic contact must have at least "
                             "3 witnesses")
        if (self.signal_strength < 7.0
                and not self.message_received):
            raise ValueError("Signal strength must be at least 7.0 ")

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 30)
    print("Valid contact report:")

    valid_contact: Dict[str, Any] = {
        "contact_id": "AC-2024-001",
        "timestamp": datetime.now(),
        "location": "Earth",
        "contact_type": "radio",
        "signal_strength": 8.0,
        "duration_minutes": 60,
        "witness_count": 1,
        "message_received": "Hello",
        "is_verified": True
    }

    invalid_contact: Dict[str, Any] = {
        "contact_id": "AC-2024-002",
        "timestamp": datetime.now(),
        "location": "Earth",
        "contact_type": "radio",
        "signal_strength": 1.0,
        "duration_minutes": 60,
        "witness_count": 1,
        "message_received": "",
        "is_verified": False
    }
    try:
        valid_contact = AlienContact(**valid_contact)

        print(f"ID: {valid_contact.contact_id}")
        print(f"Type: {valid_contact.contact_type.value}")
        print(f"Location: {valid_contact.location}")
        print(f"Signal: {valid_contact.signal_strength}/10")
        print(f"Duration: {valid_contact.duration_minutes} minutes")
        print(f"Witnesses: {valid_contact.witness_count}")
        print(f"Message: '{valid_contact.message_received}'\n")
    except ValidationError as e:
        print(f"Invalid contact report: {e.errors()[0]['msg']}")

    print("=" * 30)
    print("Expected validation error:")

    try:
        invalid_contact = AlienContact(**invalid_contact)
    except ValidationError as e:
        print(e.errors()[0]['ctx']['error'])


if __name__ == "__main__":
    main()
