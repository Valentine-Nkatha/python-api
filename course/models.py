from django.db import models

# Create your models here.
class Course(models.Model):
    name =  models.CharField(max_length=20)
    code= models.PositiveSmallIntegerField
    instructor=models.CharField(max_length=20)
    assignment=models.CharField(max_length=20)
    level= models.CharField(max_length=20)
    department= models.CharField(max_length=20)
    description=models.TextField
    syllabus= models.PositiveIntegerField
    exams = models.CharField(max_length=20)
    duration=models.CharField(max_length=20)

    objects = models.Manager()
    
    def __str__(self) -> str:
        return f"{self.name} {self.instructor}"