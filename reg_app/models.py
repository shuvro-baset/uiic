from django.db import models


class Student(models.Model):
    st_id = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=50)


class CourseRegistration(models.Model):
    TYPE = (
        ('REGULAR', 'REGULAR'),
        ('RETAKE', 'RETAKE'),
    )

    stu_name = models.CharField(max_length=30)
    st_id = models.CharField(max_length=20, null=False, blank=False)
    stu_type = models.CharField(max_length=30, choices=TYPE, default=TYPE[0])
    department = models.CharField(max_length=20, null=False, blank=False)
    semester = models.CharField(max_length=20, null=False, blank=False)
    semester_name = models.CharField(max_length=20, null=False, blank=False)
    credit = models.CharField(max_length=20, null=False, blank=False)


class CourseEnroll(models.Model):
    STATUS = (
        ('REGULAR', 'REGULAR'),
        ('RETAKE', 'RETAKE'),
    )
    student = models.ForeignKey(CourseRegistration, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=20, null=False, blank=False)
    course_code = models.CharField(max_length=20, null=False, blank=False)
    credit_hour = models.CharField(max_length=20, null=False, blank=False)
    status = models.CharField(max_length=30, choices=STATUS, default=STATUS[0])
    remarks = models.BooleanField(default=False)
