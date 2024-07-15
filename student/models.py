from django.db import models

# Create your models here.
class Students(models.Model):
    first_name =  models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    code =models.PositiveSmallIntegerField()
    email=models.EmailField()
    age= models.PositiveIntegerField()
    country= models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)
    date_of_birth= models.DateField()
    immediate_contact = models.CharField(max_length=20)
    bio = models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

