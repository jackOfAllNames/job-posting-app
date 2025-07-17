from django.urls import path
from .views import index, job_details

urlpatterns = [
    path('', index, name='home'),
    path('job/<int:pk>/', job_details, name='job-detail')
]