from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from rest_framework import generics


class Creatingstudent(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = Studentserializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ListClassBase(generics.ListCreateAPIView):
    serializer_class = Studentserializer

    def get_queryset(self):
        name = self.kwargs.get("name")
        return Student.objects.filter(class_name__icontains=name)


class List_all(generics.ListCreateAPIView):
    serializer_class = Studentserializer
    queryset = Student.objects.all().order_by("class_name")


class Namebasesearch(generics.ListCreateAPIView):
    serializer_class = Studentserializer

    def get_queryset(self):
        name = self.kwargs.get("name")
        return Student.objects.filter(name=name)


class Addingteacher(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = Teacherserializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Subjectcreate(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = Subjectserializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Subjectall(generics.ListCreateAPIView):
    serializer_class = Subjectserializerall
    queryset = Subject.objects.all()
