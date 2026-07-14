# interview-scheduling-candidate-tracking-system
FastAPI Interview Scheduling &amp; Candidate Tracking System with JWT Authentication, Candidate Management, Interview Scheduling, Feedback Management, Reports, Search, SQLAlchemy ORM, Pagination, Logging, Docker Support, and Unit Tests.
# Interview Scheduling & Candidate Tracking System

## Features

- JWT Authentication
- Candidate Management (CRUD)
- Interview Scheduling
- Feedback Management
- Reports & Search
- SQLAlchemy ORM
- SQLite Database
- Docker Support
- Logging
- Basic Unit Tests



## Setup Instructions

### Install Dependencies


pip install -r requirements.txt


### Run Project


py -m uvicorn main:app --reload


Swagger


http://127.0.0.1:8000/docs


## Environment Variables


SECRET_KEY=interview_secret_key
ALGORITHM=HS256


## API Examples

- POST `/auth/register`
- POST `/auth/login`
- POST `/candidates`
- POST `/interviews`
- POST `/feedback`



## Docker Deployment


docker build -t interview-system .
docker run -p 8000:8000 interview-system


## Assumptions

- Candidate email must be unique.
- Duplicate interview schedules are prevented for the same interviewer, date, and time.
- Feedback can only be submitted after an interview is completed.
- Ratings must be between 1 and 5.
