from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Time,
    ForeignKey
)

from database import Base


class Interview(Base):

    __tablename__ = "interviews"

    id = Column(
        Integer,
        primary_key=True
    )

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id")
    )

    interviewer_id = Column(Integer)

    interview_date = Column(Date)

    interview_time = Column(Time)

    interview_mode = Column(String)

    status = Column(String)
