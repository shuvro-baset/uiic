import pydoc

from django.conf import settings
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from io import StringIO
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .forms import CreateStuForm
from .models import CourseEnroll, StudentRegistration
from django.core.mail import EmailMessage


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        print("I am here now")
        if 'user' in request.session:
            st = request.session['user']

            st_ins = StudentRegistration.objects.filter(id=st).exists()

            print("st", st)
            print(st_ins)
            request.session._mutable = True
            # request.session['user'] = st

            st = request.session['user']

            context = {'st_ins': st_ins, 'st': st}
            return render(request, self.template_name, context=context)


class LogView(View):
    template_name = 'login.html'

    def post(self, request):
        st_id = request.POST.get('st_id')
        password = request.POST.get('password')

        is_st = StudentRegistration.objects.filter(st_id=st_id, password=password).exists()
        print(is_st)

        if is_st:

            student = StudentRegistration.objects.filter(st_id=st_id).first()
            request.session._mutable = True
            request.session['user'] = student.id
            print("logged in successfully")
            return redirect('/home')
        else:

            student = StudentRegistration(st_id=st_id, password=password, )
            student.save()
            request.session._mutable = True
            request.session['user'] = student.id

            st = request.session['user']
            st_ins = StudentRegistration.objects.filter(id=st).first()
            student = StudentRegistration.objects.filter(st_id=st_id).first()
            request.session._mutable = True
            request.session['user'] = student.id

            print(request.session['user'])
            return redirect('/home')

    def get(self, request):
        return render(request, self.template_name)


class CourseRegView(View):
    template_name = 'course_reg.html'

    def post(self, request):
        st = request.session['user']
        st_ins = StudentRegistration.objects.filter(id=st).first()

        course_enroll_ins = CourseEnroll.objects.filter(student=st_ins.id).first()
        print(course_enroll_ins)
        if not st_ins:
            return redirect('/home')

        stu_name = request.POST.get('stu_name')
        st_id = request.POST.get('st_id')
        stu_type = request.POST.get('stu_type')
        print(stu_type)
        department = request.POST.get('department')
        semester = request.POST.get('semester')
        semester_name = request.POST.get('semester_name')
        credit = request.POST.get('credit')

        st_ins.stu_name = stu_name
        st_ins.st_id = st_id
        st_ins.stu_type = stu_type.upper()
        print("student type: ", st_ins.stu_type)
        st_ins.department = department
        st_ins.semester = semester
        st_ins.semester_name = semester_name

        st_ins.credit = credit
        st_ins.save()
        # course enroll info
        courses = request.POST.getlist('subjects')
        print(courses)
        for data in courses:
            if data == 'Chemistry':
                enroll_ins1 = CourseEnroll(student=st_ins, course_name=data, course_code='CHEM-2301',
                                           credit_hour=3,
                                           status=request.POST.get('che_status'))
                enroll_ins1.save()
            elif data == 'Computer Programing lab-1':
                enroll_ins2 = CourseEnroll(student=st_ins, course_name=data, course_code='CSE-1122', credit_hour=1.5,
                                           status=request.POST.get('prg_status'))
                enroll_ins2.save()
            elif data == 'Sciences of Quran Hadith':
                enroll_ins3 = CourseEnroll(student=st_ins, course_name=data, course_code='CSE-1122', credit_hour=1,
                                           status=request.POST.get('prg_status'))
                enroll_ins3.save()
            elif data == 'Data Structure':
                enroll_ins4 = CourseEnroll(student=st_ins, course_name=data, course_code='CSE-1122', credit_hour=3,
                                           status=request.POST.get('prg_status'))
                enroll_ins4.save()
            elif data == 'Data Structure lab':
                enroll_ins5 = CourseEnroll(student=st_ins, course_name=data, course_code='CSE-1122', credit_hour=1,
                                           status=request.POST.get('prg_status'))
                enroll_ins5.save()
            elif data == 'Digital Logic Design':
                enroll_ins6 = CourseEnroll(student=st_ins, course_name=data, course_code='CSE-1122', credit_hour=3,
                                           status=request.POST.get('prg_status'))
                enroll_ins6.save()
            elif data == 'Digital Logic Design lab':
                enroll_ins7 = CourseEnroll(student=st_ins, course_name=data, course_code='CSE-1122', credit_hour=1.5,
                                           status=request.POST.get('prg_status'))
                enroll_ins7.save()
        print(courses)
        enroll_ins = CourseEnroll.objects.filter(student=st_ins.id).all()

        message = "Student Id: " + st_id + "."\
                    "Student Name: " + stu_name + "."\
                    "Department: " + department + "."\
                    "Semester: " + semester + "." \
               " has applied for semester registration. Please review it soon."

        subject = 'Student Enroll Mail'
        to = 'k.fatima172000@gmail.com'
        email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [to])
        email.content_subtype = 'html'
        email.send()

        return redirect('/dashboard/<str:stu_id>')

    def get(self, request):
        if 'user' in request.session:
            st = request.session['user']
            st_ins = StudentRegistration.objects.filter(id=st).first()
            print(st)
            print(st_ins)
            if not st_ins:
                print("I returend from here.")
                return redirect('/home')
        return render(request, self.template_name, context={"st_ins": st_ins})


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get(self, request, stu_id):
        if 'user' in request.session:
            st = request.session['user']

            st_ins = StudentRegistration.objects.filter(id=st).first()
            stu_id = st_ins.st_id
            print(stu_id)
            enroll_ins = CourseEnroll.objects.filter(student=st_ins.id).all()
            print(st)
            print(st_ins)
            if not st_ins:
                return redirect('/home')
            context = {'st_ins': st_ins, 'enroll_ins': enroll_ins}
            return render(request, self.template_name, context=context)


class ForgetPass(View):
    template_name = 'forget_pass.html'

    def post(self, request):
        st_id = request.POST.get('st_id')
        print("student: ", st_id)

        is_st = StudentRegistration.objects.filter(st_id=st_id).exists()
        print(is_st)

        if not is_st:
            message = 'Please enter your correct id'
            context = {'message': message}
            return render(request, self.template_name, context)
        else:
            student = StudentRegistration.objects.filter(st_id=st_id).first()
            request.session._mutable = True
            request.session['user'] = student.id
            return redirect('/reset-password')

    def get(self, request):
        return render(request, self.template_name)


class ResetPass(View):
    template_name = 'reset_pass.html'

    def post(self, request):
        st = request.session['user']
        print(st)
        st_ins = StudentRegistration.objects.filter(id=st).first()
        print('st_ins', st_ins)
        password = request.POST.get('password')
        print('password', password)
        st_ins.password = password
        st_ins.save()

        return redirect('/home')

    def get(self, request):
        return render(request, self.template_name)
