from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.CharField(max_length=50)
    hostel_block = models.CharField(max_length=10)
    subjects = models.ManyToManyField('Subject', blank=True)

    def __str__(self):
        return self.user.username

SLOT_CHOICES = [
    ('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'),
    ('C1', 'C1'), ('C2', 'C2'), ('D1', 'D1'), ('D2', 'D2'),
    ('F1', 'F1'), ('F2', 'F2'),
]

class Subject(models.Model):
    name = models.CharField(max_length=100)
    slots = models.CharField(max_length=2, choices=SLOT_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.slots})"

class StudySession(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    location = models.CharField(max_length=200)  # For virtual or physical locations
    platform = models.CharField(max_length=50, choices=[('Google Meet', 'Google Meet'), ('Microsoft Teams', 'Microsoft Teams'), ('IRL', 'In Real Life')])

    def __str__(self):
        return f"{self.subject.name} on {self.date} at {self.start_time}"
