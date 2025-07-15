from django.urls import path, include
from .views import index, HelloView

urlpatterns = [
    path('test/', index),
    path('hello/', HelloView.as_view(), name='hello')
]