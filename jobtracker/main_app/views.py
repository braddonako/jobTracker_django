from django.shortcuts import render
from django.http import HttpResponse


class Job:  # Note that parens are optional if not inheriting from another class
  def __init__(self, company, job_title, cover_letter, followup, notes):
    self.company = company
    self.job_title = job_title
    self.cover_letter = cover_letter
    self.followup = followup
    self.notes = notes


jobs = [
    Job('Pax8', 'Front end Engineer', 'Yes', 'no',
        'These people need to get back to me come on now'),
    Job('Pax8', 'Back end Engineer', 'Yes', 'no', 'cmon now'),
    Job('Pax8', 'Front end Engineer', 'no', 'no', 'ahha'),
]


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def jobs_index(request):
  return render(request, 'jobs/index.html', { 'jobs': jobs })
