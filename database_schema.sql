CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(50)
);

CREATE TABLE candidates(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    experience VARCHAR(50),
    skill_set VARCHAR(255),
    application_status VARCHAR(50)
);

CREATE TABLE interviews(
    id INTEGER PRIMARY KEY,
    candidate_id INTEGER,
    interviewer_id INTEGER,
    interview_date DATE,
    interview_time TIME,
    interview_mode VARCHAR(20),
    status VARCHAR(50)
);

CREATE TABLE feedback(
    id INTEGER PRIMARY KEY,
    interview_id INTEGER,
    technical_rating INTEGER,
    communication_rating INTEGER,
    remarks TEXT
);
