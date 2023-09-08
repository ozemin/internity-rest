from django.urls import path

from jobs import views

urlpatterns = [
    path('create/', views.JobCreate.as_view(), name='create'),
    path('detail/<str:pk>/', views.JobDetail.as_view(), name='detail'),
    path('list/', views.JobList.as_view(), name='list'),
    path('apply/<str:pk>/', views.JobApplicationCreate.as_view(), name='apply'),
]