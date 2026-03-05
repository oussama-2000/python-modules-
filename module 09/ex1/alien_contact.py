from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional


class Contact(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(
        min_length=5,
        max_length=15,
        description="contact ID"
        )
    timestamp: datetime
    location: str = Field(
        min_length=3,
        max_length=100,
        description="contact location"
        )
    contact_type: Contact
    signal_strength: float = Field(
        ge=0.0,
        le=10.0,
        description="signal strength"
        )
    duration_minutes: int = Field(
        ge=1,
        le=1440,
        description="duration minutes"
        )
    witness_count: int = Field(
        ge=1,
        le=100,
        description="witness count"
        )
    message_received: Optional[str] = Field(
        max_length=500,
        description="message received"
        )
    is_verified: bool = Field(
        default=False,
        description="if the contact is verified"
        )

    @model_validator(mode='after')
    def validator(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        if self.contact_type == Contact.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == Contact.telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 "
                             "witnesses")
        if not self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include received "
                             "messages")

        return self


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        valid_test = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type="radio",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
        print(
            "valid contact report:\n"
            f"ID: {valid_test.contact_id}\n"
            f"Type: {valid_test.contact_type.value}\n"
            f"Location: {valid_test.location}\n"
            f"Signal: {valid_test.signal_strength}/10\n"
            f"Duration: {valid_test.duration_minutes} minutes\n"
            f"Witnesses: {valid_test.witness_count}\n"
            f"Message: '{valid_test.message_received}'\n"
        )

        print("======================================")
        _ = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type="telepathic",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
    except ValidationError as e:
        print(f"Expected validation error:\n{e.errors()[0]['msg'][13:]}")
