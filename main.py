import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine

from routes.auth import router as auth_router
from routes.candidates import router as candidates_router
from routes.interviews import router as interviews_router
from routes.feedback import router as feedback_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Interview Scheduling & Candidate Tracking System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router)
app.include_router(candidates_router)
app.include_router(interviews_router)
app.include_router(feedback_router)


@app.get("/")
def home():

    logger.info("Application Started Successfully")

    return {
        "message": "Interview Scheduling & Candidate Tracking System"
    }
