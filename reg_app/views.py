from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from .forms import CreateStuForm
from .models import CourseEnroll, StudentRegistration


class HomeView(TemplateView):
    template_name = 'home.html'


class LogView(View):
    template_name = 'login.html'

    def post(self, request):
        # form = CreateStuForm(request.POST)
        # if form.is_valid():
        #     form.save()
        st_id = request.POST.get('st_id')
        is_st = StudentRegistration.objects.filter(st_id=st_id).exists()
        if is_st:
            message = 'Please enter different id'
            context = {'message': message}
            return render(request, self.template_name, context)
        password = request.POST.get('password')

        student = StudentRegistration(st_id=st_id, password=password, )
        student.save()

        return redirect('/home')

    def get(self, request):
        return render(request, self.template_name)


class CourseRegView(View):
    template_name = 'course_reg.html'

    def post(self, request):
        stu_name = request.POST.get('stu_name')
        st_id = request.POST.get('st_id')
        stu_type = request.POST.get('stu_type')
        department = request.POST.get('department')
        semester = request.POST.get('semester')
        semester_name = request.POST.get('semester_name')
        credit = request.POST.get('credit')

        stu_ins = StudentRegistration(stu_name=stu_name, st_id=st_id, stu_type=stu_type, department=department,
                                      semester=semester, semester_name=semester_name,
                                      credit=credit, )
        stu_ins.save()
        # course enroll info
        courses = request.POST.getlist('subjects')
        for data in courses:
            if data == 'Chemistry':
                enroll_ins = CourseEnroll(student=stu_ins, course_name=data, course_code='CHEM-2301',
                                          credit_hour=3,
                                          status=request.POST.get('che_status'))
                enroll_ins.save()
            elif data == 'Computer Programing lab-1':
                enroll_ins = CourseEnroll(student=stu_ins, course_name=data, course_code='CSE-1122', credit_hour=1.5,
                                          status=request.POST.get('prg_status'))
                enroll_ins.save()
            elif data == 'Sciences of Quran Hadith':
                enroll_ins = CourseEnroll(student=stu_ins, course_name=data, course_code='CSE-1122', credit_hour=1,
                                          status=request.POST.get('prg_status'))
                enroll_ins.save()
            elif data == 'Data Structure':
                enroll_ins = CourseEnroll(student=stu_ins, course_name=data, course_code='CSE-1122', credit_hour=3,
                                          status=request.POST.get('prg_status'))
                enroll_ins.save()
            elif data == 'Data Structure lab':
                enroll_ins = CourseEnroll(student=stu_ins, course_name=data, course_code='CSE-1122', credit_hour=1,
                                          status=request.POST.get('prg_status'))
                enroll_ins.save()
            elif data == 'Digital Logic Design':
                enroll_ins = CourseEnroll(student=stu_ins, course_name=data, course_code='CSE-1122', credit_hour=3,
                                          status=request.POST.get('prg_status'))
                enroll_ins.save()
            elif data == 'Digital Logic Design lab':
                enroll_ins = CourseEnroll(student=stu_ins, course_name=data, course_code='CSE-1122', credit_hour=1.5,
                                          status=request.POST.get('prg_status'))
                enroll_ins.save()
        print(courses)
        return redirect('/home')
        # context = {'stu_ins': stu_ins, 'enroll_ins': enroll_ins}
        #
        # return render(request, 'dashboard.html', context)

    def get(self, request):
        return render(request, self.template_name)


class DashboardView(TemplateView):
    template_name = 'dashboard.html'
