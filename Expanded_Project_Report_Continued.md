# Capture The Flag (CTF) Web Application - Continued Expanded Report

---

## 18. Detailed Code Walkthroughs

### 18.1 Models

#### CTFQuestion Model

```python
from django.db import models

class CTFQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    points = models.IntegerField(default=0)
    file = models.FileField(upload_to='question_files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text
```

- `question_text`: Stores the challenge question text.  
- `points`: Integer value representing the score for the question.  
- `file`: Optional file upload field for challenge-related files.  
- `created_at`: Timestamp for when the question was created.

#### Flag Model

```python
class Flag(models.Model):
    question = models.ForeignKey(CTFQuestion, on_delete=models.CASCADE)
    flag_text = models.CharField(max_length=255)

    def __str__(self):
        return self.flag_text
```

- Links each flag to a specific question.  
- Stores the correct flag text.

#### Participant Model

```python
class Participant(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    score = models.IntegerField(default=0)
    solved_questions = models.ManyToManyField(CTFQuestion, blank=True)

    def __str__(self):
        return self.username
```

- Stores participant credentials and score.  
- Tracks solved questions via many-to-many relationship.

---

### 18.2 Views

#### Admin Portal View (Excerpt)

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

- Handles adding new questions with optional file uploads.  
- Similar logic applies for flags and participants.

---

## 19. Diagrams

### 19.1 Entity-Relationship Diagram (ERD)

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

- One question can have multiple flags.  
- Participants can solve multiple questions (many-to-many).

---

## 20. Additional Chapters

### 20.1 Testing Strategy

- Unit tests for models and views using Django's test framework.  
- Manual testing of form submissions and session management.  
- Load testing on Render to ensure scalability.

### 20.2 Code Quality and Best Practices

- Followed PEP8 style guide for Python code.  
- Used Django's built-in security features.  
- Modularized code for maintainability.

### 20.3 Documentation and Version Control

- Used Git for version control with descriptive commit messages.  
- Hosted code on GitHub for collaboration and deployment integration.  
- Maintained detailed project documentation (this report).

---

## 21. Summary

This continued report section provides deeper insights into the codebase, database design, and project management practices. Further expansions can include detailed testing reports, user manuals, and deployment guides.

---

*End of Continued Expanded Report*

---

*Note: Diagrams are textual representations; graphical diagrams can be created using tools like draw.io or Lucidchart.*
