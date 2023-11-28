import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone


def validate_date(due_date):
    if due_date.date() < datetime.date.today():
        raise ValidationError("This date can not be in the past")


# Create your models here.
class Task(models.Model):
    title = models.CharField(
        max_length=100,
        default="Default",
        editable=True,
        blank=False,
        validators=[MinLengthValidator(limit_value=5)],
    )
    description = models.CharField(
        max_length=500,
        default="I shoud do it",
        editable=True,
        blank=True,
        validators=[MinLengthValidator(limit_value=20)],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, editable=True)
    due_date = models.DateTimeField(
        default=timezone.now, editable=True, validators=[validate_date]
    )

    PRIORITY_CHOICES = [
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    ]
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default="Medium", editable=True
    )

    @property
    def remaining_time(self):
        now = timezone.now()
        time_difference = self.due_date - now
        days = time_difference.days
        hours = int(time_difference.seconds / 3600)
        return f"{days} days and {hours} hours"

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["due_date"]
