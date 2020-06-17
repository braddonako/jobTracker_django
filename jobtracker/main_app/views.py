from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class JobCreate(CreateView):
    model = Job
    fields = '__all__'
    success_url = '/jobs/'

class JobUpdate(UpdateView):
    model = Job
    fields = ['cover_letter', 'followup', 'notes']

class JobDelete(DeleteView):
    model = Job
    success_url = '/jobs/'
