from django.db import models

#
# class Student(models.Model):
#     st_id = models.CharField(max_length=20, null=False, blank=False, unique=True)


class StudentRegistration(models.Model):
    TYPE = (
        ('REGULAR', 'REGULAR'),
        ('RETAKE', 'RETAKE'),
    )

    stu_name = models.CharField(max_length=30, null=True, blank=True)
    st_id = models.CharField(max_length=20, unique=True, null=False, blank=False)
    password = models.CharField(max_length=50)
    stu_type = models.CharField(max_length=30, null=True, blank=True, choices=TYPE, default=TYPE[0])
    department = models.CharField(max_length=20, null=True, blank=True)
    semester = models.CharField(max_length=20, null=True, blank=True)
    semester_name = models.CharField(max_length=20, null=True, blank=True)
    credit = models.CharField(max_length=20, null=True, blank=True)


class CourseEnroll(models.Model):
    STATUS = (
        ('REGULAR', 'REGULAR'),
        ('RETAKE', 'RETAKE'),
    )
    student = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=30, null=False, blank=False)
    course_code = models.CharField(max_length=20, null=False, blank=False)
    credit_hour = models.CharField(max_length=20, null=False, blank=False)
    status = models.CharField(max_length=30, choices=STATUS, default=STATUS[0])
    remarks = models.BooleanField(default=False)
