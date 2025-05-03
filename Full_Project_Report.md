# Capture The Flag (CTF) Web Application - Complete Project Report

---

## Table of Contents

1. Introduction  
2. Project Overview  
3. Technology Stack  
4. Project Setup and Development  
5. Backend Architecture and Pipeline  
6. Frontend Overview  
7. Deployment on Render  
8. Functionalities  
9. Database Models and Relationships  
10. Security Considerations  
11. Challenges and Solutions  
12. Conclusion  
13. References  
14. Expanded Details and Code Walkthroughs  
15. Diagrams  
16. Additional Chapters  
17. Deployment Deep Dive  
18. Security Enhancements  
19. User Experience (UX) Considerations  
20. Code Snippets and Explanations  
21. Project Management and Collaboration  
22. Final Thoughts and Recommendations  
23. Further Expansions: Advanced Features and Future Scope  
24. Code Quality and Maintainability  
25. Appendix  
26. Acknowledgments  
27. Contact Information  

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

## 14. Expanded Details and Code Walkthroughs

### Models

```python
from django.db import models

class CTFQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    points = models.IntegerField(default=0)
    file = models.FileField(upload_to='question_files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

class Flag(models.Model):
    question = models.ForeignKey(CTFQuestion, on_delete=models.CASCADE)
    flag_text = models.CharField(max_length=255)

    def __str__(self):
        return self.flag_text

class Participant(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    score = models.IntegerField(default=0)
    solved_questions = models.ManyToManyField(CTFQuestion, blank=True)

    def __str__(self):
        return self.username
```

### Admin Portal View (Excerpt)

```python
def admin_portal(request):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')

    if request.method == 'POST':
        if 'add_question' in request.POST:
            question_text = request.POST.get('question_text')
            points = request.POST.get('points')
            file = request.FILES.get('file')
            if question_text:
                question = CTFQuestion(question_text=question_text, points=int(points) if points else 0)
                if file:
                    question.file = file
                question.save()
        # Additional handling for flags and participants...
```

---

## 15. Diagrams

### Entity-Relationship Diagram (ERD)

```
+----------------+       +----------------+       +------------------+
|  CTFQuestion   |1     *|      Flag      |       |    Participant   |
+----------------+-------+----------------+       +------------------+
| id             |       | id             |       | id               |
| question_text  |       | flag_text      |       | username         |
| points         |       | question_id FK |       | password         |
| file           |       +----------------+       | score            |
| created_at     |                                | solved_questions*|
+----------------+                                +------------------+
```

---

## 16. Additional Chapters

### Testing Strategy

- Unit tests for models and views using Django's test framework.  
- Manual testing of form submissions and session management.  
- Load testing on Render to ensure scalability.

### Code Quality and Best Practices

- Followed PEP8 style guide for Python code.  
- Used Django's built-in security features.  
- Modularized code for maintainability.

### Documentation and Version Control

- Used Git for version control with descriptive commit messages.  
- Hosted code on GitHub for collaboration and deployment integration.  
- Maintained detailed project documentation (this report).

---

## 17. Deployment Deep Dive

### Render.com Setup

- Created a new Web Service on Render linked to the GitHub repository.  
- Configured environment variables securely via Render dashboard.  
- Set build and start commands.  
- Enabled automatic deploys on GitHub push.

### Static Files Handling

- Integrated WhiteNoise middleware to serve static files efficiently.  
- Configured `STATIC_ROOT` and `STATICFILES_DIRS` in settings.py.  
- Collected static files during deployment.

### Database Migration Automation

- Added migration commands to run automatically on app startup.

---

## 18. Security Enhancements

- Password hashing recommended for production.  
- Session security with secure cookies and HTTPS.  
- CSRF protection enabled on all forms.

---

## 19. User Experience (UX) Considerations

- Clean and modern UI using Google Fonts and custom CSS.  
- Responsive design for accessibility.  
- Inline editing and deletion in admin portal.  
- Clear feedback messages on form submissions.

---

## 20. Code Snippets and Explanations

### File Upload Handling

```python
if 'add_question' in request.POST:
    question_text = request.POST.get('question_text')
    points = request.POST.get('points')
    file = request.FILES.get('file')
    if question_text:
        question = CTFQuestion(question_text=question_text, points=int(points) if points else 0)
        if file:
            question.file = file
        question.save()
```

### Live Scoreboard JSON Response

```python
def live_scoreboard(request):
    participants = Participant.objects.all().values('username', 'score').order_by('-score')
    return JsonResponse(list(participants), safe=False)
```

---

## 21. Project Management and Collaboration

- Used Git for version control with meaningful commit messages.  
- Hosted code on GitHub for collaboration and deployment integration.  
- Maintained issue tracking and task management.

---

## 22. Final Thoughts and Recommendations

- Solid foundation for a CTF platform.  
- Future improvements: enhanced security, richer UI, real-time features.  
- Continuous documentation and testing recommended.

---

## 23. Advanced Features and Future Scope

- Real-time updates with Django Channels.  
- User registration and profile management.  
- Analytics and reporting dashboards.  
- Containerization with Docker and CI/CD pipelines.

---

## 24. Code Quality and Maintainability

- Adopt linting tools like flake8 and black.  
- Write comprehensive tests.  
- Use Django logging for monitoring.

---

## 25. Appendix

### Sample .env File

```
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://user:password@host:port/dbname
ALLOWED_HOSTS=yourdomain.com,127.0.0.1
DEBUG=False
```

### Useful Commands

- Run migrations: `python manage.py migrate`  
- Create superuser: `python manage.py createsuperuser`  
- Collect static files: `python manage.py collectstatic`  
- Run development server: `python manage.py runserver`

---

## 26. Acknowledgments

- Django community for excellent documentation.  
- Render.com for deployment services.  
- Open source contributors.

---

## 27. Contact Information

**Your Name**  
Email: 23020700329@reva.edu.in  
GitHub: https://github.com/Tanush-Jain

---

*End of Complete Project Report*
