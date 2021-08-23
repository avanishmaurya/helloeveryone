from django.urls import path
from app1 import views


urlpatterns = [
    path('', views.studentInfo_list, name="studentInfo_list"),
    path('studentInfo_detail/<int:pk>/', views.studentInfo_detail, name="studentInfo_detail"),

]
