from datetime import date
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

REVIEW_CHOICES = {
    ("Y", "Yes"),
    ("N", "No")
}

CADENCE_CHOICES = {
    ("Daily", "Daily"),
    ("Weekly", "Weekly"),
    ("Bi-Weekly", "Bi-Weekly"),
    ("Monthly", "Monthly"),
}


class Report(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    cadence = models.CharField(max_length=50, choices = CADENCE_CHOICES)
    date = models.DateField(max_length=100)
    notes = models.TextField(max_length=300, blank=True)
    reviewed = models.CharField(max_length=10, choices = REVIEW_CHOICES)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Location(models.Model):

    name = models.CharField(max_length=50)
    location_number = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    reports = models.ManyToManyField(Report, blank=True)

    def __str__(self):
        return self.name

    class Meta: 
        ordering = ['name']