from sqlalchemy import (
    Column,
    Integer,
    String
)

from database import Base


class Candidate(Base):

    __tablename__ = "candidates"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(String)

    email = Column(
        String,
        unique=True
    )

    phone = Column(String)

    experience = Column(String)

    skill_set = Column(String)

    application_status = Column(String)
