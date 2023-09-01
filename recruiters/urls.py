from django.urls import path

from recruiters import views

urlpatterns = [
    path('register/', views.RecruiterRegister.as_view()),
    path('login/', views.RecruiterLogin.as_view()),
    path('profile/register/', views.RecruiterProfileRegister.as_view()),
    path('profile/', views.RecruiterProfile.as_view()),
]
