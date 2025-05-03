# Capture The Flag (CTF) Web Application Project Report

---

## Table of Contents

1. Introduction  
2. Project Overview  
3. Technology Stack  
4. Project Setup and Development  
   - Initial Setup with SQLite3  
   - Transition to PostgreSQL  
5. Backend Architecture and Pipeline  
6. Frontend Overview  
7. Deployment on Render  
8. Functionalities  
   - Admin Portal  
   - Participant Portal  
   - Live Scoreboard  
9. Database Models and Relationships  
10. Security Considerations  
11. Challenges and Solutions  
12. Conclusion  
13. References  

---

## 1. Introduction

This report documents the development of a Capture The Flag (CTF) web application built using Django. The project was designed to provide a platform for cybersecurity enthusiasts to participate in CTF challenges, submit flags, and track scores in real-time. The application supports two types of users: Admins and Participants.

---

## 2. Project Overview

The CTF web application allows admins to create and manage questions, flags, and participants. Participants can log in, attempt challenges by submitting flags, and view their scores. The system maintains a live scoreboard to display participant rankings.

---

## 3. Technology Stack

- **Backend Framework:** Django (Python)  
- **Frontend:** Django Templates, HTML, CSS, JavaScript  
- **Database:** Initially SQLite3, later migrated to PostgreSQL  
- **Deployment Platform:** Render.com  
- **Other Tools:** Gunicorn (WSGI server), WhiteNoise (static file serving), dj-database-url (database URL parsing), python-dotenv (environment variables management)

---

## 4. Project Setup and Development

### Initial Setup with SQLite3

- The project was initially set up using Django's default SQLite3 database for rapid development and testing.
- Models for `CTFQuestion`, `Flag`, and `Participant` were created.
- Basic views and templates were developed to support user interactions.

### Transition to PostgreSQL

- To prepare for production deployment, the database was migrated from SQLite3 to PostgreSQL.
- PostgreSQL was chosen for its robustness, scalability, and compatibility with Render.com.
- The `dj-database-url` package was used to parse the database URL from environment variables.
- Migrations were applied to PostgreSQL to ensure data integrity.

---

## 5. Backend Architecture and Pipeline

- **Models:**  
  - `CTFQuestion`: Stores challenge questions, points, and optional files.  
  - `Flag`: Stores the correct flag associated with each question.  
  - `Participant`: Stores user credentials and scores, along with solved questions.

- **Views:**  
  - Admin views handle login, logout, and management of questions, flags, and participants.  
  - Participant views handle login, challenge attempts, and score tracking.  
  - Live scoreboard views provide real-time participant rankings.

- **Session Management:**  
  - Django sessions are used to manage user authentication states.

- **File Uploads:**  
  - Admins can upload files related to questions, stored and served securely.

---

## 6. Frontend Overview

- The frontend uses Django templates with custom CSS for styling.
- Responsive and user-friendly interfaces were created for both admin and participant portals.
- Forms are used for login, adding/editing questions, flags, and participants.
- The live scoreboard updates participant rankings dynamically.

---

## 7. Deployment on Render

- The project was deployed on Render.com, a cloud platform for hosting web applications.
- Environment variables such as `SECRET_KEY`, `DATABASE_URL`, and `ALLOWED_HOSTS` were configured securely.
- Gunicorn was used as the WSGI server to serve the Django application.
- WhiteNoise was integrated to serve static files efficiently.
- Automatic migrations were configured to run on startup to keep the database schema up to date.

---

## 8. Functionalities

### Admin Portal

- Secure login with session management.
- Add, edit, and delete CTF questions, flags, and participants.
- Upload files associated with questions.
- View all participants and their scores.
- Manage the entire CTF challenge lifecycle.

### Participant Portal

- Secure login for participants.
- View available challenges and submit flags.
- Track personal scores and progress.
- Access downloadable files related to challenges.

### Live Scoreboard

- Displays real-time rankings of participants based on scores.
- Accessible to all users to foster competition.

---

## 9. Database Models and Relationships

- `CTFQuestion` has a one-to-many relationship with `Flag`.
- `Participant` has a many-to-many relationship with `CTFQuestion` through solved questions.
- Scores are updated dynamically based on correct flag submissions.

---

## 10. Security Considerations

- Passwords are stored securely (note: in this project, password hashing should be implemented for production).
- Session management prevents unauthorized access.
- CSRF protection is enabled on all forms.
- Environment variables are used to secure sensitive information.
- Allowed hosts are configured to prevent host header attacks.

---

## 11. Challenges and Solutions

- **Database Migration:** Transitioning from SQLite3 to PostgreSQL required careful migration of data and updating configurations.
- **File Upload Handling:** Ensuring secure and efficient file uploads for challenge files.
- **Deployment Issues:** Configuring Render.com environment variables, static file serving with WhiteNoise, and Gunicorn setup.
- **Admin Portal Functionality:** Implementing full CRUD operations for questions, flags, and participants with proper form handling.

---

## 12. Conclusion

This project demonstrates the development of a full-stack web application using Django, showcasing skills in backend development, database management, frontend templating, and cloud deployment. The CTF platform is functional, scalable, and ready for further enhancements.

---

## 13. References

- Django Documentation: https://docs.djangoproject.com/  
- Render.com Documentation: https://render.com/docs  
- WhiteNoise Documentation: http://whitenoise.evans.io/en/stable/  
- PostgreSQL Documentation: https://www.postgresql.org/docs/  

---

*End of Report*
