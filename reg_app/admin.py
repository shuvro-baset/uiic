from django.contrib import admin

# Register your models here.
from reg_app.models import CourseRegistration, CourseEnroll

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_filter = ('id', 'st_id',)
    list_display = ('st_id',)


@admin.register(CourseRegistration)
class CourseRegistrationAdmin(admin.ModelAdmin):
    list_filter = ('id', 'st_id',)
    list_display = ('st_id',)


@admin.register(CourseEnroll)
class CourseEnrollAdmin(admin.ModelAdmin):
    list_filter = ('id', 'course_name',)
    list_display = ('course_name',)
