from django.db import models
from teachers.models import Teacher
from classes.models import Class
from course.models import Course

# Create your models here.
class ClassPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField(max_length=20, default="Python")
    period = models.IntegerField(default=3)
    day_of_week = models.CharField(max_length=20, default="Monday")
    # teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_perod_id = models.ForeignKey(Class, on_delete=models.CASCADE,default=0)
    courses = models.ManyToManyField(Course)
    teacher = models .ManyToManyField(Teacher)

    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.course} {self.start_time}"

