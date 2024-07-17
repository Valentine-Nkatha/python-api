from django.db import models

from teacher.models import Teacher

# Create your models here.
class ClassPeriod(models.Model):
    class_id = models.AutoField(primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField(max_length=20)
    classroom_period = models.CharField(max_length=20, default="classes")
    day_of_week = models.CharField(max_length=20)
    teachers_period = models.ForeignKey(Teacher, on_delete=models.CASCADE,related_name="teachers")

    objects = models.Manager()

    def __str__(self):
        return f"{self.course} {self.start_time}"

