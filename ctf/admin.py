from django.contrib import admin
from .models import CTFQuestion, Flag, Participant

admin.site.register(CTFQuestion)
admin.site.register(Flag)
admin.site.register(Participant)
