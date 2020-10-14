from django.forms import ModelForm
from django import forms

from .models import Student


class CreateStuForm(ModelForm):
    class Meta:
        model = Student
        fields = ['st_id','password',]