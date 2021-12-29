from django.db import models


# Create your models here.

class Student(models.Model):
    stu_name = models.CharField(max_length=264)
    stu_age = models.IntegerField()
    stu_subject = models.CharField(max_length=264)
    stu_country = models.CharField(max_length=264)

    def __str__(self):
        return self.stu_name
