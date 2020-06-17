from django.db import models
from django.urls import reverse
# Create your models here.

class Job(models.Model):
    company= models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    cover_letter = models.TextField(max_length=1000)
    followup = models.TextField(max_length=1000)
    notes = models.TextField(max_length=1000)

    
    def __str__(self):
        return self.company
    
    def get_absolute_url(self):
       return reverse('detail', kwargs={'job_id': self.id})
