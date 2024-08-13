from django.db import models

from teachers.models import Teacher

# Create your models here.
class ClassPeriod(models.Model):
    start_time = models.TimeField()
    class_perod_id = models.AutoField(primary_key=True)
    end_time = models.TimeField()
    course = models.CharField(max_length=20, default="Python")
    period = models.IntegerField()
    day_of_week = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,related_name="teachers")
    # teachers = models.ManyToManyField(Teacher)

    objects = models.Manager()

    def __str__(self):
        return f"{self.course} {self.start_time}"

