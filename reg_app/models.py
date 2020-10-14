from django.db import models


class Student(models.Model):
    st_id = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=50)