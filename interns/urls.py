from django.urls import path

from interns import views

urlpatterns = [
    path('register/', views.InternRegister.as_view(), name='register'),
    path('login/', views.InternLogin.as_view(), name='login'),
    path('register/profile/', views.InternProfileRegister.as_view(), name='register-profile'),
    path('profile/', views.InternProfile.as_view(), name='profile'),
    path('logout/', views.InternLogout.as_view(), name='logout'),
]