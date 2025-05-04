# Capture The Flag (CTF) Web Application

## Table of Contents

1. [Introduction](#introduction)  
2. [Project Overview](#project-overview)  
3. [Technology Stack](#technology-stack)  
4. [Project Setup and Development](#project-setup-and-development)  
5. [Backend Architecture and Pipeline](#backend-architecture-and-pipeline)  
6. [Frontend Overview](#frontend-overview)  
7. [Deployment on Render](#deployment-on-render)  
8. [Functionalities](#functionalities)  
9. [Database Models and Relationships](#database-models-and-relationships)  
10. [Security Considerations](#security-considerations)  
11. [Challenges and Solutions](#challenges-and-solutions)  
12. [Conclusion](#conclusion)  
13. [References](#references)  
14. [Contact Information](#contact-information)  

---

## Introduction

This project is a Capture The Flag (CTF) web application built using Django. It provides a platform for cybersecurity enthusiasts to participate in CTF challenges, submit flags, and track scores in real-time. The application supports two types of users: Admins and Participants.

---

## Project Overview

- Admins can create and manage questions, flags, and participants.
- Participants can log in, attempt challenges by submitting flags, and view their scores.
- A live scoreboard displays participant rankings in real-time.

---

## Technology Stack

- **Backend Framework:** Django (Python)  
- **Frontend:** Django Templates, HTML, CSS, JavaScript  
- **Database:** Initially SQLite3, migrated to PostgreSQL  
- **Deployment Platform:** Render.com  
- **Other Tools:** Gunicorn, WhiteNoise, dj-database-url, python-dotenv

---

## Project Setup and Development

- Started with SQLite3 for rapid development.
- Migrated to PostgreSQL for production readiness.
- Models include `CTFQuestion`, `Flag`, and `Participant`.
- Views handle admin and participant functionalities.
- Session management and CSRF protection enabled.
- File uploads supported for challenge files.

---

## Backend Architecture and Pipeline

- Models represent questions, flags, and participants with relationships.
- Admin views manage CRUD operations for challenges and users.
- Participant views handle login, flag submissions, and score tracking.
- Live scoreboard provides real-time rankings.

---

## Frontend Overview

- Uses Django templates with custom CSS for styling.
- Responsive and user-friendly interfaces for admin and participants.
- Forms for login, adding/editing questions, flags, and participants.
- Dynamic live scoreboard updates.

---

## Deployment on Render

- Hosted on Render.com with environment variables configured.
- Gunicorn used as WSGI server.
- WhiteNoise serves static files efficiently.
- Automatic migrations run on startup.

---

## Functionalities

### Admin Portal

- Secure login and session management.
- Manage questions, flags, participants.
- Upload files for challenges.
- View participant scores.

### Participant Portal

- Secure login.
- View and attempt challenges.
- Track scores and progress.
- Download challenge files.

### Live Scoreboard

- Real-time participant rankings.
- Publicly accessible.

---

## Database Models and Relationships

- `CTFQuestion` has many `Flag`s.
- `Participant` has many solved questions.
- Scores update dynamically on correct submissions.

---

## Security Considerations

- Passwords stored securely (recommend hashing for production).
- Session and CSRF protections enabled.
- Environment variables secure sensitive data.
- Allowed hosts configured.

---

## Challenges and Solutions

- Database migration from SQLite3 to PostgreSQL.
- Secure file upload handling.
- Deployment configuration on Render.
- Full CRUD operations in admin portal.

---

## Conclusion

This project demonstrates a full-stack Django application for CTF challenges, showcasing backend, frontend, and deployment skills. It is scalable and ready for further enhancements.

---

## References

- [Django Documentation](https://docs.djangoproject.com/)  
- [Render.com Documentation](https://render.com/docs)  
- [WhiteNoise Documentation](http://whitenoise.evans.io/en/stable/)  
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

## Contact Information

**Your Name**  
Email: 23020700329@reva.edu.in  
GitHub: [https://github.com/Tanush-Jain](https://github.com/Tanush-Jain)

---

*Thank you for exploring this project!*
