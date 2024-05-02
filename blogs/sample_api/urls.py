from .views import StudentView
from django.urls import path
from django.urls import include, re_path

urlpatterns = [
    path('basic/', StudentView.as_view()),  
    path('basic/<int:id>/', StudentView.as_view()),  
    path('basic/<int:id>/update/', StudentView.as_view()) 
]
