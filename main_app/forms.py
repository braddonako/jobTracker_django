from django.forms import ModelForm
from .models import Note, Job

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['date', 'comment', 'update']


