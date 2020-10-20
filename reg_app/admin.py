from django.contrib import admin


from .models import StudentRegistration, CourseEnroll

# 
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_filter = ('id', 'st_id',)
#     list_display = ('st_id',)


@admin.register(StudentRegistration)
class StudentRegistrationAdmin(admin.ModelAdmin):
    list_filter = ('id', 'st_id',)
    list_display = ('st_id',)


@admin.register(CourseEnroll)
class CourseEnrollAdmin(admin.ModelAdmin):
    list_filter = ('id', 'course_name',)
    list_display = ('course_name',)
