from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home, name='home'),
    path('students_list',views.students_list, name='students_list'),
    path('Student_Marks', views.Student_Marks, name='Student_Marks'),
    path('Check', views.Check, name='Check'),
path('home', views.home, name='Home'),

]