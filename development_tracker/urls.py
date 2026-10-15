from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('complaint/<int:pk>/', views.complaint_detail, name='complaint_detail'),
    path('complaint/add/', views.add_complaint, name='add_complaint'),
]
