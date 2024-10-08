from django.db import models

# from student.models import Students

# Create your models here.
class Course(models.Model):
    # course_id = models.SmallIntegerField(primary_key=True)
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
    # students = models.ManyToManyField(Students)

    objects = models.Manager()
    
    def __str__(self) -> str:
        return f"{self.name} {self.instructor}"