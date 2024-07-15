from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Students
from .serializer import StudentSerializer
from rest_framework.response import Response
from classperiod.models import ClassPeriod
from .serializer import ClassPeriodSerializer
from rest_framework import serializers
# Create your views here.
class StudentListView(APIView):
      def get(self, request):
            students = Students.objects.all()
            serializer=StudentSerializer(students, many=True)
            return Response(serializer.data)
      
class ClassPeriodListView(APIView):
      def get(self, request):
          periods = ClassPeriod.objects.all()
          serializer=ClassPeriodSerializer(periods, many=True)
          return Response(serializer.data)