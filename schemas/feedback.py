from pydantic import (
    BaseModel,
    Field
)


class FeedbackCreate(BaseModel):

    interview_id: int

    technical_rating: int = Field(..., ge=1, le=5)

    communication_rating: int = Field(..., ge=1, le=5)

    remarks: str = Field(..., min_length=5)
