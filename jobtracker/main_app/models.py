from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from datetime import date


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
    company= models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    cover_letter = models.CharField(max_length=750)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.company
    
    def get_absolute_url(self):
       return reverse('detail', kwargs={'job_id': self.id})

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
