from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    #通知列表设有一个标志位来标志是否已读，0为未读，1为已读，前端点击了通知详情按钮后，应该到后台将状态设置为已读
    GlobalNoticeList = [['1', '操作系统课程有新通知', '2017/12/12, 20:00:00', '作业1已发布，ddl为今晚10点'],
                  ['1', '计算机网络课程有新通知', '2017/12/13, 20:00:00', '作业2已发布，ddl为今晚10点'],
                  ['0', '软件需求工程课程有新通知', '2017/12/14, 20:00:00', '作业3已发布，ddl为今晚10点'],
                  ['0', '操作系统课程有新通知', '2017/12/14, 20:00:00', '作业4已发布，ddl为今晚10点']]
    unreadGlobalNotice = 0
    for i in GlobalNoticeList:
        if i[0] == '0':
            unreadGlobalNotice += 1
    #课程表，应统计每门课程未读通知+未提交的作业数量
    CoursesList = [['软件需求工程', ['邢卫', '刘玉生'], '周一6，7，8', '专业课', '2'],
                   ['操作系统原理', ['伍赛'], '周一6，7，8', '专业课', '1'],
                   ['软件工程管理', ['金波'], '周一6，7，8', '专业课', '1'],
                   ['计算机网络', ['陆魁军'], '周一6，7，8', '专业课', '0'],]
    return render(request, 'student/index.html',{'GlobalNoticeList': GlobalNoticeList,
                                                 'unreadGlobalNotice': unreadGlobalNotice,
                                                 'CoursesList': CoursesList})


def course(request):
    #论坛贴子列表
    PostList = [['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                ['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                ['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0']]
    #通知列表设有一个标志位来标志是否已读，0为未读，1为已读，前端点击了通知详情按钮后，应该到后台将状态设置为已读
    NoticeList = [['1','作业1已发布', '2017/12/12, 20:00:00', '作业1已发布，ddl为今晚10点'],
                  ['1','作业2已发布', '2017/12/13, 20:00:00', '作业2已发布，ddl为今晚10点'],
                  ['0','作业3已发布', '2017/12/14, 20:00:00', '作业3已发布，ddl为今晚10点'],
                  ['0','作业4已发布', '2017/12/14, 20:00:00', '作业4已发布，ddl为今晚10点']]
    unreadNotice = 0
    for i in NoticeList:
        if i[0] == '0':
            unreadNotice+=1
    #作业列表设有一个标志位来标志是否已提交，0为未提交，1为已提交，前端提交作业后，应该到后台将状态设置为已提交；
    #应能正确指导前端进行页面跳转
    HwList = [['1', '作业1', '2017/12/12, 20:00:00'],
              ['1', '作业2', '2017/12/13, 20:00:00'],
              ['0', '作业3', '2017/12/14, 20:00:00']]
    unsubmitHw = 0
    for i in HwList:
        if i[0] == '0':
            unsubmitHw+=1
    #教师信息表
    TeacherList = [['邢卫', '教授', '计算机科学与技术学院', '10086@zju.edu.cn', '18888888888'],
                   ['邢卫', '教授', '计算机科学与技术学院', '10086@zju.edu.cn', '18888888888'],
                   ]
    #资源列表
    ResoursesList = [['uml.ppt', '刘玉生', '2017/12/12, 20:00:00'],
                     ['5.ppt', '刘玉生', '2017/12/12, 20:00:00'],
                     ['操作系统概念.pdf', '王泽杰', '2017/12/12, 20:00:00'],
                     ['软件需求.pdf', '邢卫', '2017/12/12, 20:00:00'],
                     ['作业成绩.xls', '邢卫', '2017/12/12, 20:00:00']]
    return render(request, 'student/student_courses.html', {'PostList': PostList,
                                                            'NoticeList': NoticeList,'unreadNotice': unreadNotice,
                                                            'HwList': HwList, 'unsubmitHw': unsubmitHw,
                                                            'TeacherList': TeacherList,
                                                            'ResoursesList': ResoursesList})


def hw(request):
    return render(request, 'student/student_hw.html')


def forum(request):
    return render(request, 'student/student_forum.html')


def ret(request):
    return render(request, 'login.html')