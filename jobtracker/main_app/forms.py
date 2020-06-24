from django.forms import ModelForm
from django import forms
from .models import Note, Job
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['date', 'comment', 'update']


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
