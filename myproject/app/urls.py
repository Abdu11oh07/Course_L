
from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),  
    path('courses/<int:course_id>/lessons/', views.lesson_list, name='lesson_list'),
    path('lessons/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
]

