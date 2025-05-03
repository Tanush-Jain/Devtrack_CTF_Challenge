# Capture The Flag (CTF) Web Application - Expanded Project Report

---

## Table of Contents

1. Introduction  
2. Project Objectives and Scope  
3. Technology Stack Overview  
4. Development Environment Setup  
5. Initial Project Setup and Architecture  
6. Database Design and Models  
7. Backend Development  
   - Views and URL Routing  
   - Session and Authentication Management  
   - File Upload Handling  
8. Frontend Development  
   - Template Structure and Styling  
   - User Interface Design Considerations  
9. Transition from SQLite3 to PostgreSQL  
   - Reasons for Migration  
   - Migration Process and Challenges  
10. Deployment Strategy  
    - Render.com Platform Overview  
    - Environment Configuration  
    - Static Files Management with WhiteNoise  
    - Gunicorn Setup  
11. Functional Features  
    - Admin Portal Functionalities  
    - Participant Portal Functionalities  
    - Live Scoreboard Implementation  
12. Security Measures  
    - Authentication and Authorization  
    - Data Validation and Sanitization  
    - Environment Variable Management  
13. Testing and Debugging  
14. Challenges Faced and Solutions Implemented  
15. Future Enhancements and Recommendations  
16. Conclusion  
17. References and Resources  

---

## 1. Introduction

This document provides an in-depth report on the development of a Capture The Flag (CTF) web application using Django. The project was undertaken to build a secure, scalable, and user-friendly platform for cybersecurity enthusiasts to participate in challenges, submit flags, and track their progress.

---

## 2. Project Objectives and Scope

- Develop a web-based CTF platform with distinct roles for admins and participants.  
- Implement CRUD operations for challenges, flags, and participants.  
- Enable secure authentication and session management.  
- Provide real-time score tracking and leaderboard display.  
- Deploy the application on a cloud platform with production-ready configurations.

---

## 3. Technology Stack Overview

- **Django Framework:** Chosen for its rapid development capabilities, built-in admin interface, and robust ORM.  
- **Python:** Backend programming language.  
- **SQLite3:** Initial lightweight database for development and testing.  
- **PostgreSQL:** Production-grade database for deployment.  
- **Render.com:** Cloud platform for hosting the application.  
- **Gunicorn:** WSGI HTTP server for UNIX.  
- **WhiteNoise:** Simplifies static file serving in production.  
- **HTML/CSS/JavaScript:** Frontend technologies for UI development.

---

## 4. Development Environment Setup

- Installed Python 3.11 and Django 4.2.20.  
- Set up virtual environments to isolate dependencies.  
- Configured Git for version control and GitHub for remote repository hosting.  
- Installed PostgreSQL locally for testing migration scripts.

---

## 5. Initial Project Setup and Architecture

- Created a new Django project named `ctf_app`.  
- Created an app within the project named `ctf` to encapsulate CTF-related functionalities.  
- Defined project structure adhering to Django best practices.  
- Configured settings.py for initial SQLite3 database usage.

---

## 6. Database Design and Models

- **CTFQuestion Model:**  
  - Fields: `question_text` (CharField), `points` (IntegerField), `file` (FileField, optional).  
  - Purpose: Stores challenge questions and associated metadata.

- **Flag Model:**  
  - Fields: `flag_text` (CharField), ForeignKey to `CTFQuestion`.  
  - Purpose: Stores correct flags for challenges.

- **Participant Model:**  
  - Fields: `username` (CharField), `password` (CharField), `score` (IntegerField), ManyToMany relation to solved questions.  
  - Purpose: Stores participant credentials and progress.

---

## 7. Backend Development

### Views and URL Routing

- Implemented views for home, admin login/logout, participant login, admin portal, participant page, and live scoreboard.  
- Used Django's URL dispatcher to map URLs to views.

### Session and Authentication Management

- Used Django sessions to manage login states for admins and participants.  
- Implemented simple authentication logic with session flags.

### File Upload Handling

- Enabled file uploads for challenge questions.  
- Configured media root and URL in settings.py.  
- Handled file saving and serving securely.

---

## 8. Frontend Development

### Template Structure and Styling

- Used Django templates for dynamic HTML rendering.  
- Created separate templates for admin login, admin portal, participant login, participant page, home, and live scoreboard.  
- Applied custom CSS with Google Fonts for a modern look.

### User Interface Design Considerations

- Focused on usability and clarity.  
- Used forms with CSRF protection for security.  
- Provided inline editing and deletion options in admin portal.

---

## 9. Transition from SQLite3 to PostgreSQL

### Reasons for Migration

- SQLite3 is suitable for development but lacks scalability and concurrency for production.  
- PostgreSQL offers robustness, advanced features, and better performance.

### Migration Process and Challenges

- Installed PostgreSQL and configured connection via `dj-database-url`.  
- Updated settings.py to use PostgreSQL in production.  
- Applied Django migrations to PostgreSQL database.  
- Addressed data type and constraint differences.  
- Tested thoroughly to ensure data integrity.

---

## 10. Deployment Strategy

### Render.com Platform Overview

- Chosen for ease of use, free tier availability, and integration with GitHub.  
- Supports Python and Django deployments with environment variable management.

### Environment Configuration

- Set environment variables for `SECRET_KEY`, `DATABASE_URL`, `ALLOWED_HOSTS`, and `DJANGO_SETTINGS_MODULE`.  
- Used `.env` files locally and Render dashboard for production.

### Static Files Management with WhiteNoise

- Integrated WhiteNoise middleware for efficient static file serving.  
- Configured static root and storage settings.

### Gunicorn Setup

- Used Gunicorn as the WSGI server for production.  
- Configured Procfile to launch Gunicorn with the correct WSGI application.

---

## 11. Functional Features

### Admin Portal Functionalities

- Secure login with session management.  
- Add, edit, delete questions, flags, and participants.  
- Upload files for questions.  
- View participant scores and manage users.

### Participant Portal Functionalities

- Secure login and session management.  
- View available challenges and submit flags.  
- Track scores and progress.  
- Access downloadable challenge files.

### Live Scoreboard Implementation

- Real-time display of participant rankings.  
- Accessible to all users to encourage competition.

---

## 12. Security Measures

- Used Django's CSRF protection on all forms.  
- Managed sensitive data via environment variables.  
- Implemented session-based authentication.  
- Passwords stored in plain text for demo; recommend hashing for production.  
- Configured allowed hosts to prevent host header attacks.

---

## 13. Testing and Debugging

- Performed unit testing on models and views.  
- Used Django's debug mode for local testing.  
- Monitored logs on Render for runtime errors.  
- Fixed issues related to migrations, static files, and deployment.

---

## 14. Challenges Faced and Solutions Implemented

- Database migration complexities from SQLite3 to PostgreSQL.  
- Handling file uploads securely.  
- Configuring deployment environment variables and static files.  
- Implementing full CRUD operations in admin portal.

---

## 15. Future Enhancements and Recommendations

- Implement password hashing and stronger authentication.  
- Add user registration and email verification.  
- Enhance UI with React or Vue.js for better interactivity.  
- Add real-time WebSocket-based scoreboard updates.  
- Implement detailed analytics and reporting.

---

## 16. Conclusion

This project demonstrates a full-stack Django application development lifecycle, from initial setup to deployment. It highlights key skills in backend development, database management, frontend templating, and cloud deployment, making it a strong portfolio project for job interviews.

---

## 17. References and Resources

- Django Official Documentation: https://docs.djangoproject.com/  
- Render.com Documentation: https://render.com/docs  
- WhiteNoise Documentation: http://whitenoise.evans.io/en/stable/  
- PostgreSQL Documentation: https://www.postgresql.org/docs/  

---

*End of Expanded Report*

---

*Note: This report can be further expanded with detailed code snippets, diagrams, and step-by-step walkthroughs as needed.*
