from django.db import models

# Create your models here.

class Job(models.Model):
    company= models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    cover_letter = models.BooleanField(default=False)
    followup = models.BooleanField(default=False)
    notes = models.TextField(max_length=1000)

    
