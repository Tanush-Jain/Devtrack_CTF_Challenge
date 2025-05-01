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
    password = models.CharField(max_length=128, null=True, blank=True)  # Allow null for migration
    score = models.IntegerField(default=0)
    solved_questions = models.ManyToManyField(CTFQuestion, blank=True, related_name='solved_by')

    def __str__(self):
        return self.username
