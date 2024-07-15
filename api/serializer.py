from rest_framework import serializers;
from student.models import Students;
from classperiod.models import ClassPeriod;

class StudentSerializer (serializers. ModelSerializer):
    class Meta:
                model=Students
                fiels =" __all__"
class ClassPeriodSerializer(serializers.ModelSerializer):
        class Meta:
                model = ClassPeriod
                fields = '__all__'
