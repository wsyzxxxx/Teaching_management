from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'teacher/index.html')


def course(request):
    PostList = [['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                 ['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                 ['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0']]
    return render(request, 'teacher/teacher_course.html', {'PostList': PostList})


def hw(request):
    return render(request, 'teacher/teacher_hw.html')


def new_hw(request):
    return render(request, 'teacher/new_hw.html')


def teacher_forum(request):
    return render(request, 'teacher/teacher_forum.html')