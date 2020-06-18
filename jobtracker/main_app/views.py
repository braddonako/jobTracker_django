from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Job
from .forms import NoteForm


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

    note_form = NoteForm()
    return render(request, 'jobs/detail.html', {
        'job': job, 'note_form': note_form
    })

def add_note(request, job_id):
    form = NoteForm(request.POST)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.job_id = job_id
        new_note.save()
    return redirect('detail', job_id=job_id)


class JobCreate(CreateView):
    model = Job
    fields = '__all__'
    success_url = '/jobs/'

class JobUpdate(UpdateView):
    model = Job
    fields = ['referral']

class JobDelete(DeleteView):
    model = Job
    success_url = '/jobs/'
