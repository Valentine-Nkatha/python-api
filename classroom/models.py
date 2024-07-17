from django.db import models

# Create your models here.
class Class(models.Model):
    class_time =  models.DateTimeField
    class_capacity= models.PositiveSmallIntegerField
    class_name =models.CharField(max_length=20)
    class_lecturer=models.CharField(max_length=20)
    class_id= models.PositiveSmallIntegerField
    class_name= models.CharField(max_length=20)
    class_rep=models.CharField(max_length=20)
    class_description= models.TextField
    electricity = models.CharField(max_length=20)
    class_attendance=models.PositiveSmallIntegerField

    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.class_name} {self.class_lecturer}"
