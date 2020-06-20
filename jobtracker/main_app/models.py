from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from datetime import date
from django.utils import timezone


# Create your models here.

UPDATES = (
    ('u', 'Update'),
    ('!', 'Important!!!'),
    ('p', 'Phone Screen'),
    ('f', 'Follow up'),
    ('c', 'The job has been closed'),
    ('i','Interview')
)

class Job(models.Model):
    date = models.DateField('Date applied', default=timezone.now())
    company= models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default='')
    comment = models.TextField(max_length=250, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
       return f"{self.company} on {self.date}"

    def get_absolute_url(self):
       return reverse('detail', kwargs={'job_id': self.id})

    class Meta:
        ordering = ['-date']

class Note(models.Model):
    date = models.DateField('Date posted')
    comment= models.TextField(max_length=250, default='')
    update = models.CharField(
        max_length=2,
        choices=UPDATES,
        default=UPDATES[0][0]    
    )
    

    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_update_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Upload(models.Model):
    url = models.CharField(max_length=200)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cover letter for job_id: {self.job_id} @{self.url}"
