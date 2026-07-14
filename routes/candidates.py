from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal

from models.candidate import Candidate

from schemas.candidate import CandidateCreate

from services.interview_service import valid_phone

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_candidate(
    candidate: CandidateCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(Candidate).filter(
        Candidate.email == candidate.email
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Candidate email already exists."
        )

    if not valid_phone(candidate.phone):

        raise HTTPException(
            status_code=400,
            detail="Phone number must contain exactly 10 digits."
        )

    new_candidate = Candidate(
        name=candidate.name,
        email=candidate.email,
        phone=candidate.phone,
        experience=candidate.experience,
        skill_set=candidate.skill_set,
        application_status=candidate.application_status
    )

    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)

    return new_candidate


@router.get("/")
def get_candidates(
    skill_set: str = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Candidate)

    if skill_set:
        query = query.filter(
            Candidate.skill_set.contains(skill_set)
        )

    total = query.count()

    candidates = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total,
        "current_page": page,
        "limit": limit,
        "data": candidates
    }


@router.get("/{candidate_id}")
def get_candidate(
    candidate_id: int,
    db: Session = Depends(get_db)
):

    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:

        raise HTTPException(
            status_code=404,
            detail="Candidate not found."
        )

    return candidate


@router.put("/{candidate_id}")
def update_candidate(
    candidate_id: int,
    candidate: CandidateCreate,
    db: Session = Depends(get_db)
):

    db_candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not db_candidate:

        raise HTTPException(
            status_code=404,
            detail="Candidate not found."
        )

    db_candidate.name = candidate.name
    db_candidate.email = candidate.email
    db_candidate.phone = candidate.phone
    db_candidate.experience = candidate.experience
    db_candidate.skill_set = candidate.skill_set
    db_candidate.application_status = candidate.application_status

    db.commit()

    return {
        "message": "Candidate updated successfully."
    }


@router.delete("/{candidate_id}")
def delete_candidate(
    candidate_id: int,
    db: Session = Depends(get_db)
):

    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:

        raise HTTPException(
            status_code=404,
            detail="Candidate not found."
        )

    db.delete(candidate)

    db.commit()

    return {
        "message": "Candidate deleted successfully."
    }
