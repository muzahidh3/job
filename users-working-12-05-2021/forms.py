from django import forms
from django.contrib.auth import authenticate
from django.db import transaction
from .models import User, Profile
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2', 'email', 'division_name')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('location'),