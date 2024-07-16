from rest_framework import serializers;
from student.models import Students;
from classperiod.models import ClassPeriod;
from course.models import Course
from teacher.models import Teacher


class StudentSerializer (serializers. ModelSerializer):
    class Meta:
                model=Students
                fields = '__all__'
class ClassPeriodSerializer(serializers.ModelSerializer):
        class Meta:
                model = ClassPeriod
                fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
        class Meta:
                model=Course
                fields = '__all__'
class TeacherSerializer(serializers.ModelSerializer):
        class Meta:
                model = Teacher
                fields = '__all__'