from rest_framework import serializers;
from student.models import Students;
from classperiod.models import ClassPeriod;
from course.models import Course
from teachers.models import Teacher
from classes.models import Class


# class StudentSerializer (serializers. ModelSerializer):
# #     class Meta:
# #                 model=Students
# #                 fields = '__all__'

#         courses = CourseSerializer(many=True)
#         class Meta:
#                model = Students
#                fields = '__all__'
class minimalClassPeriodSerializer(serializers.ModelSerializer):
        # class Meta:
        #         model = Students
        #         fields = ["first_name","email"]
        start_time = serializers.SerializerMethodField()
        def get_start_time(self,object):
                return object.start_time
        
        class Meta:
                 model = Students
                 fields = ["start_time"]

class ClassPeriodSerializer(serializers.ModelSerializer):
        class Meta:
                model = ClassPeriod
                fields = '__all__'
class minimalCoursesSerializer(serializers.ModelSerializer):
        # class Meta:
        #         model = Students
        #         fields = ["first_name","email"]
        name = serializers.SerializerMethodField()
        def get_name(self,object):
                return object.name
        
        class Meta:
                 model = Students
                 fields = ["name"]

class CourseSerializer(serializers.ModelSerializer):
        class Meta:
                model=Course
                fields = '__all__'
class minimalTeacherSerializer(serializers.ModelSerializer):
        # class Meta:
        #         model = Students
        #         fields = ["first_name","email"]
        teacher_gender = serializers.SerializerMethodField()
        def get_teacher_gender(self,object):
                return object.teacher_gender
        
        class Meta:
                 model = Students
                 fields = ["teacher_gender"]
class TeacherSerializer(serializers.ModelSerializer):
        class Meta:
                model = Teacher
                fields = '__all__'
class minimalClassSerializer(serializers.ModelSerializer):
        # class Meta:
        #         model = Students
        #         fields = ["first_name","email"]
        class_lecturer = serializers.SerializerMethodField()

        def get_class_lecturer(self,object):
                return object.class_lecturer
        
        class Meta:
                 model = Students
                 fields = ["class_lecturer"]
class ClassSerializer(serializers.ModelSerializer):
        class Meta:
                model = Class
                fields = '__all__'

class minimalStudentSerializer(serializers.ModelSerializer):
        # class Meta:
        #         model = Students
        #         fields = ["first_name","email"]
        full_name = serializers.SerializerMethodField()
        def get_full_name(self,object):
                return f"{object.first_name} {object.last_name}"
        
        class Meta:
                 model = Students
                 fields = ["full_name", "email"]
class StudentSerializer (serializers. ModelSerializer):
#     class Meta:
#                 model=Students
#                 fields = '__all__'

        courses = CourseSerializer(many=True)
        classes = ClassSerializer(many=True)
        class Meta:
               model = Students
               fields = '__all__'
               
               
        