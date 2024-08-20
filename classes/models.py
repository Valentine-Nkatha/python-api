from django.db import models
from django.utils import timezone
from student.models import Students

# Create your models here.
class Class(models.Model):
    class_time =  models.DateTimeField(default=timezone.now)
    class_capacity= models.PositiveSmallIntegerField(default=35)
    class_name =models.CharField(max_length=20, default="Adalab")
    class_lecturer=models.CharField(max_length=20, default="John")
    class_rep=models.CharField(max_length=20, default="Nancy")
    class_description= models.TextField(default="It is class full of girls")
    class_performance = models.FloatField(default=0)
    class_attendance=models.PositiveSmallIntegerField(default=30)
    class_code = models.PositiveSmallIntegerField(default=10)
    class_students = models.ManyToManyField(Students)

    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.class_name} {self.class_lecturer}"
