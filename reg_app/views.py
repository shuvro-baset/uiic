from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from .forms import CreateStuForm
from .models import Student, CourseEnroll, CourseRegistration


class HomeView(TemplateView):
    template_name = 'home.html'


class LogView(View):
    template_name = 'login.html'

    def post(self, request):
        form = CreateStuForm(request.POST)
        if form.is_valid():
            form.save()
            # students = Student.objects.all()
            # return render(request, {'students': students})
        return redirect('/home')

    def get(self, request):
        return render(request, self.template_name)


class CourseRegView(View):
    template_name = 'course_reg.html'

    def post(self, request):
        stu_name = request.POST.get('stu_name')

        stu_ins = CourseRegistration(stu_name=stu_name,st_id=st_id,stu_type=stu_type,department=department,semester=semester,semester_name=semester_name,
                                     credit=credit, )
        stu_ins.save()
        # course enroll info
        courses = request.POST.getlist('subjects')
        for data in courses:
            if data == 'Chemistry':
                enroll_ins = CourseEnroll(student=stu_ins, course_name=data, course_code='CHEM-2301',
                                          status=request.POST.get('che_status'))
                enroll_ins.save()
            elif data == 'Computer Programing lab-1':
                enroll_ins = CourseEnroll(student=stu_ins, course_name=data, course_code='CSE-1122',
                                          status=request.POST.get('prg_status'))
                enroll_ins.save()
        print(courses)

        return redirect('/home')

    def get(self, request):
        return render(request, self.template_name)


class DashboardView(TemplateView):
    template_name = 'dashboard.html'
