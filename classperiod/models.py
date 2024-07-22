from django.db import models

from teacher.models import Teacher

# Create your models here.
class ClassPeriod(models.Model):
    start_time = models.TimeField()
    class_perod_id = models.AutoField(primary_key=True)
    end_time = models.TimeField()
    course = models.CharField(max_length=20, default="Python")
    period = models.CharField(max_length=20, default="one year")
    day_of_week = models.CharField(max_length=20)
    # teachers_period = models.ForeignKey(Teacher, on_delete=models.CASCADE,related_name="teachers")
    teacherss = models.ManyToManyField(Teacher)

    objects = models.Manager()

    def __str__(self):
        return f"{self.course} {self.start_time}"

