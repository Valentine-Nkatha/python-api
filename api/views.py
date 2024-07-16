from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Students
from .serializer import StudentSerializer
from rest_framework.response import Response
from classperiod.models import ClassPeriod
from .serializer import ClassPeriodSerializer
from rest_framework import serializers
from course.models import Course
from .serializer import CourseSerializer
from  .serializer import TeacherSerializer
from teacher.models import Teacher


# Create your views here.
class StudentListView(APIView):
      def get(self, request):
            students = Students.objects.all()
            serializer=StudentSerializer(students, many=True)
            return Response(serializer.data)
      
class ClassPeriodListView(APIView):
      def get(self, request):
          classperiods = ClassPeriod.objects.all()
          serializer=ClassPeriodSerializer(classperiods, many=True)
          return Response(serializer.data)

class CourseListView(APIView):
      def get(self, request):
            courses = Course.objects.all()
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)
class TeacherListView(APIView):
      def get(self, request):
            teachers = Teacher.objects.all()
            serializer = TeacherSerializer(teachers, many=True)
            return Response(serializer.data)