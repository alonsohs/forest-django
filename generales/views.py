from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home1(request):
    return HttpResponse("Hola Mundo desde Django")


def home(request):
    return render(request, 'index.html')


