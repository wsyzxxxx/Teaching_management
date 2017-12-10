from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def course(request):
    return render(request, 'student_courses.html')

def ret(request):
    return render(request, 'login.html')