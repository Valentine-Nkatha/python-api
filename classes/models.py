from django.db import models

# Create your models here.
class Class(models.Model):
    classroom_id = models.AutoField
    class_time =  models.DateTimeField
    class_capacity= models.PositiveSmallIntegerField
    class_name =models.CharField(max_length=20)
    class_lecturer=models.CharField(max_length=20, default="John")
    # class_id= models.PositiveSmallIntegerField
    class_name= models.CharField(max_length=20, default="Adalab")
    class_rep=models.CharField(max_length=20, default="Nancy")
    class_description= models.TextField
    class_performance = models.FloatField(default=0)
    class_attendance=models.PositiveSmallIntegerField

    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.class_name} {self.class_lecturer}"
