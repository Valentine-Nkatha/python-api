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
from classroom.models import Class
from .serializer import ClassSerializer
from rest_framework import status


# Create your views here.
class StudentListView(APIView):
      def get(self, request):
            students = Students.objects.all()
            serializer=StudentSerializer(students, many=True)
            return Response(serializer.data)
      
      def post(self, request):
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class StudentDetailView(APIView):
      def get(self,request,id):
            student = Students.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
      def put(self, request,id):
            student = Students.objects.get(id=id)
            serializer = StudentSerializer(student,data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      def delete(self,request,id):
            student = Students.objects.get(id=id)
            student.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
            
      

            


class ClassPeriodListView(APIView):
      def get(self, request):
          classperiods = ClassPeriod.objects.all()
          serializer=ClassPeriodSerializer(classperiods, many=True)
          return Response(serializer.data)
      def post(self, request):
            serializer = ClassSerializer(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ClassPeriodDetailView(APIView):
      def get(self,request,id):
            classperiod = ClassPeriod.objects.get(id=id)
            serializer = ClassPeriodSerializer(classperiod)
            return Response(serializer.data)
      def put(self, request,id):
            classperiod = ClassPeriod.objects.get(id=id)
            serializer = ClassPeriodSerializer(classperiod,data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      def delete(self,request,id):
            classperiod =ClassPeriod.objects.get(id=id)
            classperiod.delete()
            return Response(status=status.HTTP_202_ACCEPTED)

class CourseListView(APIView):
      def get(self, request):
            courses = Course.objects.all()
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)
      def post(self, request):
            serializer = CourseSerializer(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CourseDetailView(APIView):
      def get(self,request,id):
            course = Course.objects.get(id=id)
            serializer = CourseSerializer(course)
            return Response(serializer.data)
      def put(self, request,id):
            course = Course.objects.get(id=id)
            serializer = CourseSerializer(course,data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      def delete(self,request,id):
            course =Course.objects.get(id=id)
            course.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
      

class TeacherListView(APIView):
      def get(self, request):
            teachers = Teacher.objects.all()
            serializer = TeacherSerializer(teachers, many=True)
            return Response(serializer.data)
      def post(self, request):
            serializer = TeacherSerializer(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TeacherDetailView(APIView):
      def get(self,request,id):
            teacher = Teacher.objects.get(id=id)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data)
      def put(self, request,id):
            teacher = Teacher.objects.get(id=id)
            serializer = TeacherSerializer(teacher,data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      def delete(self,request,id):
            teacher =Course.objects.get(id=id)
            teacher.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
      
class ClassListView(APIView):
      def get(self, request):
            classes = Class.objects.all()
            serializer = ClassSerializer(classes, many=True)
            return Response(serializer.data)
      def post(self, request):
            serializer = ClassSerializer(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ClassDetailView(APIView):
      def get(self,request,id):
            classs = Class.objects.get(id=id)
            serializer = ClassSerializer(classs)
            return Response(serializer.data)
      def put(self, request,id):
            classs = Class.objects.get(id=id)
            serializer = ClassSerializer(classs,data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      def delete(self,request,id):
            classs =Class.objects.get(id=id)
            classs.delete()
            return Response(status=status.HTTP_202_ACCEPTED)