from pydantic import (
    BaseModel,
    Field
)

from datetime import date, time


class InterviewCreate(BaseModel):

    candidate_id: int

    interviewer_id: int

    interview_date: date

    interview_time: time

    interview_mode: str

    status: str
