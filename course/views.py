from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views, status
from .models import Course
from .serializers import CourseSerializer


class CourseView(views.APIView):

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class CourseDetialView(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            course = Course.objects.get(id=kwargs['course_id'])
        except Course.DoesNotExist:
            return Response({"data":"Course Not Found!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        try:
            course = Course.objects.get(id=kwargs['course_id'])
        except Course.DoesNotExist:
            return Response({"data":"Course Not Found!"}, status=status.HTTP_404_NOT_FOUND)
        course.delete()
        return Response({"data":"Deleted!"})



