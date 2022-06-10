from django.urls import path, include
from .views import CourseView, CourseDetialView
urlpatterns = [
    path('courses/', CourseView.as_view(), name = 'courses'),
    path('courses/<int:course_id>/', CourseDetialView.as_view(), name = 'course')

]