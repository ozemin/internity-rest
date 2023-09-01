from django.urls import path

from companies import views

urlpatterns = [
    path('register/', views.CompanyRegister.as_view(), name='register'),
    path('profile/', views.CompanyProfile.as_view(), name='profile'),
    ]
