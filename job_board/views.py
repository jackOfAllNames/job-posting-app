from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h2>Hello to Job Board!</h2>')
