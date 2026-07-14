from pydantic import (
    BaseModel,
    EmailStr,
    Field
)


class CandidateCreate(BaseModel):

    name: str = Field(..., min_length=3)

    email: EmailStr

    phone: str = Field(..., min_length=10, max_length=10)

    experience: str

    skill_set: str

    application_status: str
