from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'teacher/index.html')


def course(request):
    return render(request, 'teacher/teacher_course.html')