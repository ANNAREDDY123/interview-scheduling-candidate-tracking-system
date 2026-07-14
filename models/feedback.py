from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from database import Base


class Feedback(Base):

    __tablename__ = "feedback"

    id = Column(
        Integer,
        primary_key=True
    )

    interview_id = Column(
        Integer,
        ForeignKey("interviews.id")
    )

    technical_rating = Column(Integer)

    communication_rating = Column(Integer)

    remarks = Column(String)
