from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class LogView(TemplateView):
    template_name = 'login.html'


class CourseRegView(TemplateView):
    template_name = 'course_reg.html'


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

