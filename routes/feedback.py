from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal

from models.feedback import Feedback
from models.interview import Interview

from schemas.feedback import FeedbackCreate

router = APIRouter(
    prefix="/feedback",
    tags=["Feedback"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_feedback(
    feedback: FeedbackCreate,
    db: Session = Depends(get_db)
):

    interview = db.query(Interview).filter(
        Interview.id == feedback.interview_id
    ).first()

    if not interview:

        raise HTTPException(
            status_code=404,
            detail="Interview not found."
        )

    if interview.status != "Completed":

        raise HTTPException(
            status_code=400,
            detail="Feedback can only be added after interview completion."
        )

    new_feedback = Feedback(
        interview_id=feedback.interview_id,
        technical_rating=feedback.technical_rating,
        communication_rating=feedback.communication_rating,
        remarks=feedback.remarks
    )

    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)

    return new_feedback


@router.get("/{interview_id}")
def get_feedback(
    interview_id: int,
    db: Session = Depends(get_db)
):

    feedback = db.query(Feedback).filter(
        Feedback.interview_id == interview_id
    ).first()

    if not feedback:

        raise HTTPException(
            status_code=404,
            detail="Feedback not found."
        )

    return feedback
