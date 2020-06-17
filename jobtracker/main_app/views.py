from django.shortcuts import render
from .models import Job


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def jobs_index(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/index.html', { 'jobs': jobs })

def jobs_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'jobs/detail.html', {'job': job})