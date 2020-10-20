from django.forms import ModelForm
from django import forms

from .models import StudentRegistration


class CreateStuForm(ModelForm):
    class Meta:
        model = StudentRegistration
        fields = ['st_id', 'password', ]


class CourseRegForm(ModelForm):
    class Meta:
        model = StudentRegistration
        fields = ['stu_name', 'st_id', 'stu_type', 'department', 'semester', 'semester_name', 'credit', ]
