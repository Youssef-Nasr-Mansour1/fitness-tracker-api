# activities/models.py
from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    ACTIVITY_CHOICES = [
        ('Running', 'Running'),
        ('Cycling', 'Cycling'),
        ('Weightlifting', 'Weightlifting'),
        # Add other activity types here
    ]

    user = models.ForeignKey(User, related_name='activities', on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    distance = models.FloatField(help_text="Distance in km or miles")
    calories_burned = models.FloatField(help_text="Calories burned")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} - {self.date.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        ordering = ['-date']
