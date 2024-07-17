from django.db import models

# Create your models here.
class Teacher(models.Model):
    teachers_name =  models.CharField(max_length=20)
    teachers_age= models.PositiveSmallIntegerField
    teachers_national_id =models.AutoField(primary_key=True)
    teachers_course=models.CharField(max_length=20)
    teachers_class= models.CharField(max_length=20)
    teachers_description= models.TextField()
    teachers_occupation=models.CharField(max_length=20)
    teachers_salary= models.PositiveIntegerField
    teaachers_hobby = models.CharField(max_length=20,default="teaching")
    teachers_gender=models.CharField(max_length=20)
    
    objects = models.Manager()
    
    def __str__(self) -> str:
        return f"{self.teachers_name} {self.teachers_age}"

