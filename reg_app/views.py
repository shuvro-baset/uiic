from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import CreateStuForm
from .models import Student


class HomeView(TemplateView):
    template_name = 'home.html'


class LogView(TemplateView):
    template_name = 'login.html'

    def log(request):
        form = CreateStuForm()
        if request.method == 'POST':
            form = CreateStuForm(request.POST)
            if form.is_valid():
                form.save()
                students = Student.objects.all()
                return render(request,  {'students': students})
        return redirect('home')




class CourseRegView(TemplateView):
    template_name = 'course_reg.html'


class DashboardView(TemplateView):
    template_name = 'dashboard.html'
