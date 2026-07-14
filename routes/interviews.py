from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal

from models.interview import Interview
from models.candidate import Candidate

from schemas.interview import InterviewCreate

from services.interview_service import (
    valid_interview_status,
    valid_interview_mode
)

router = APIRouter(
    prefix="/interviews",
    tags=["Interviews"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_interview(
    interview: InterviewCreate,
    db: Session = Depends(get_db)
):

    candidate = db.query(Candidate).filter(
        Candidate.id == interview.candidate_id
    ).first()

    if not candidate:

        raise HTTPException(
            status_code=404,
            detail="Candidate not found."
        )

    duplicate = db.query(Interview).filter(
        Interview.interviewer_id == interview.interviewer_id,
        Interview.interview_date == interview.interview_date,
        Interview.interview_time == interview.interview_time
    ).first()

    if duplicate:

        raise HTTPException(
            status_code=400,
            detail="Interviewer already has an interview scheduled at this date and time."
        )

    if not valid_interview_mode(interview.interview_mode):

        raise HTTPException(
            status_code=400,
            detail="Invalid interview mode."
        )

    if not valid_interview_status(interview.status):

        raise HTTPException(
            status_code=400,
            detail="Invalid interview status."
        )

    new_interview = Interview(
        candidate_id=interview.candidate_id,
        interviewer_id=interview.interviewer_id,
        interview_date=interview.interview_date,
        interview_time=interview.interview_time,
        interview_mode=interview.interview_mode,
        status=interview.status
    )

    db.add(new_interview)
    db.commit()
    db.refresh(new_interview)

    return new_interview


@router.get("/")
def get_interviews(
    interviewer_id: int = None,
    status: str = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Interview)

    if interviewer_id:
        query = query.filter(
            Interview.interviewer_id == interviewer_id
        )

    if status:
        query = query.filter(
            Interview.status == status
        )

    total = query.count()

    interviews = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total,
        "current_page": page,
        "limit": limit,
        "data": interviews
    }


@router.get("/{interview_id}")
def get_interview(
    interview_id: int,
    db: Session = Depends(get_db)
):

    interview = db.query(Interview).filter(
        Interview.id == interview_id
    ).first()

    if not interview:

        raise HTTPException(
            status_code=404,
            detail="Interview not found."
        )

    return interview


@router.put("/{interview_id}")
def update_interview(
    interview_id: int,
    interview: InterviewCreate,
    db: Session = Depends(get_db)
):

    db_interview = db.query(Interview).filter(
        Interview.id == interview_id
    ).first()

    if not db_interview:

        raise HTTPException(
            status_code=404,
            detail="Interview not found."
        )

    db_interview.interview_date = interview.interview_date
    db_interview.interview_time = interview.interview_time
    db_interview.interview_mode = interview.interview_mode
    db_interview.status = interview.status

    db.commit()

    return {
        "message": "Interview updated successfully."
    }
