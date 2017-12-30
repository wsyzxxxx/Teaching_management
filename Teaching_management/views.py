from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from teacher.models import UserInfo, TeacherInfo, StudentInfo, ManagerInfo, CourseInfo, \
    CourseTime, Homework, MultipleChoice, ShortAnswer, HwOfCourse, \
    StudentAnswer, HwGrade, ForumList, PostReply, Source, Message, \
    Announcement, Customer, IsRead

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    #print(username)
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
    # Correct password, and the user is marked "active"
        auth.login(request, user)
    # Redirect to a success page.
        if user.userinfo.user_type == 1:
            return HttpResponseRedirect("/student/")
        elif user.userinfo.user_type == 2:
            return HttpResponseRedirect('/teacher/')
        elif user.userinfo.user_type == 3:
            return HttpResponseRedirect('/administrater/')
        return HttpResponse("Invalid username or password")
    else:
    # Show an error page
        print(user)
        return HttpResponse("Invalid username or password")

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

