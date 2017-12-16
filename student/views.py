from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'student/index.html')


def course(request):
    PostList = [['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                ['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                ['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0']]
    return render(request, 'student/student_courses.html', {'PostList': PostList})


def hw(request):
    return render(request, 'student/student_hw.html')


def forum(request):
    return render(request, 'student/student_forum.html')


def ret(request):
    return render(request, 'login.html')