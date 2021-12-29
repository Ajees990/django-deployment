from django.urls import re_path

from student_app import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'student/', views.student, name='student'),
    re_path(r'form/', views.student_view, name='form'),
]
