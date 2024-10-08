from django.db import models
from course.models import Course

# Cretate your models here.
class Students(models.Model):
    first_name =  models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    code =models.PositiveSmallIntegerField()
    email=models.EmailField()
    age= models.PositiveIntegerField(default=20)
    country= models.CharField(max_length=20, default="Kenya")
    phone_number=models.CharField(max_length=20)
    date_of_birth= models.DateField()
    immediate_contact = models.CharField(max_length=20)
    bio = models.CharField(max_length=20, default="student")
    courses = models.ManyToManyField(Course)
    # classes = models.ForeignKey(Class, on_delete=models.CASCADE, default=1)

    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

