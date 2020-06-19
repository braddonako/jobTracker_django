from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage

from .models import Job
from .forms import NoteForm

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/login.html', context)

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


# @login_required
class JobCreate(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['date', 'company', 'position']

    def form_valid(self, form):
        form.instance.user = self.request.user  # form.instance is the job
        return super().form_valid(form)


class JobUpdate(LoginRequiredMixin, UpdateView):
    model = Job
    fields = ['position', 'company', 'location', 'comment']


class JobDelete(LoginRequiredMixin, DeleteView):
    model = Job
    success_url = '/jobs/'


@login_required
def jobs_index(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'jobs/index.html', { 'jobs': jobs })


@login_required
def jobs_detail(request, job_id):
    job = Job.objects.get(id=job_id)

    note_form = NoteForm()
    return render(request, 'jobs/detail.html', {
        'job': job, 'note_form': note_form
    })

@login_required
def add_note(request, job_id):
    form = NoteForm(request.POST)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.job_id = job_id
        new_note.save()
    return redirect('detail', job_id=job_id)

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        print(uploaded_file.name)
        print(uploaded_file.file)
    return render(request, 'upload.html')



