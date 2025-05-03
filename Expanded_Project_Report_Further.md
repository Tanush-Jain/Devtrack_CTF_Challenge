# Capture The Flag (CTF) Web Application - Further Expanded Report

---

## 22. Deployment Deep Dive

### 22.1 Render.com Setup

- Created a new Web Service on Render linked to the GitHub repository.  
- Configured environment variables securely via Render dashboard:  
  - `SECRET_KEY` for Django security.  
  - `DATABASE_URL` for PostgreSQL connection.  
  - `ALLOWED_HOSTS` to restrict host headers.  
  - `DJANGO_SETTINGS_MODULE` to specify settings.  
- Set build and start commands:  
  - Build: `pip install -r requirements.txt`  
  - Start: `gunicorn ctf_app.wsgi`  
- Enabled automatic deploys on GitHub push.

### 22.2 Static Files Handling

- Integrated WhiteNoise middleware to serve static files efficiently without needing a separate server.  
- Configured `STATIC_ROOT` and `STATICFILES_DIRS` in settings.py.  
- Collected static files during deployment.

### 22.3 Database Migration Automation

- Added migration commands to run automatically on app startup to avoid manual intervention.  
- Ensured migrations are idempotent and safe for production.

---

## 23. Security Enhancements

### 23.1 Password Management

- Current implementation stores passwords in plain text for demonstration.  
- Recommended to implement Django’s built-in password hashing using `AbstractBaseUser` or `User` model.  
- Future work includes adding password reset and email verification.

### 23.2 Session Security

- Sessions are secured with Django’s default settings.  
- Consider enabling HTTPS and secure cookies in production.

### 23.3 CSRF Protection

- All forms include CSRF tokens to prevent cross-site request forgery.

---

## 24. User Experience (UX) Considerations

- Clean and modern UI using Google Fonts and custom CSS.  
- Responsive design for accessibility on various devices.  
- Inline editing and deletion in admin portal for efficiency.  
- Clear feedback messages on form submissions.

---

## 25. Code Snippets and Explanations

### 25.1 File Upload Handling in Admin Portal

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

- Retrieves file from `request.FILES`.  
- Associates uploaded file with the question model.  
- Saves the question with file reference.

### 25.2 Live Scoreboard JSON Response

```python
def live_scoreboard(request):
    participants = Participant.objects.all().values('username', 'score').order_by('-score')
    return JsonResponse(list(participants), safe=False)
```

- Returns participant scores ordered descendingly as JSON.  
- Enables frontend to fetch and display live rankings.

---

## 26. Project Management and Collaboration

- Used Git for version control with meaningful commit messages.  
- Hosted code on GitHub for easy collaboration and deployment integration.  
- Maintained issue tracking and task management (if applicable).

---

## 27. Final Thoughts and Recommendations

- The project serves as a solid foundation for a CTF platform.  
- Future improvements include enhanced security, richer UI, and real-time features using WebSockets.  
- Documentation and testing should be continuously updated.

---

*End of Further Expanded Report*

---

*Note: For graphical diagrams and flowcharts, consider using external tools and embedding images in the report.*
