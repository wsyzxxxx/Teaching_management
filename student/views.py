from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import auth

def studentcheck(user):
    try:
        if user.userinfo.user_type == 1:
            return True
    except:
        return False
    return False

# Create your views here.
@user_passes_test(studentcheck, login_url="/login")
def index(request):
    print(request.user)
    tmp = []
    # 通知列表设有一个标志位来标志是否已读，0为未读，1为已读，前端点击了通知详情按钮后，应该到后台将状态设置为已读
    GlobalNoticeList = [['1', '操作系统课程有新通知', '2017/12/12, 20:00:00', '作业1已发布，ddl为今晚10点'],
                        ['1', '计算机网络课程有新通知', '2017/12/13, 20:00:00', '作业2已发布，ddl为今晚10点'],
                        ['0', '软件需求工程课程有新通知', '2017/12/14, 20:00:00', '作业3已发布，ddl为今晚10点'],
                        ['0', '操作系统课程有新通知', '2017/12/14, 20:00:00', '作业4已发布，ddl为今晚10点']]
    unreadGlobalNotice = 0
    for i in GlobalNoticeList:
        if i[0] == '0':
            unreadGlobalNotice += 1
    # 课程表，应统计每门课程未读通知、未完成作业、未阅读课件的数量
    CoursesList = [['软件需求工程', ['邢卫', '刘玉生'], ['周一6，7，8'], ['玉泉曹光彪西-503', '玉泉教7-304(多)'], '专业课', '2', '1', '1'],
                   ['操作系统原理', ['伍赛'], ['周一6，7，8'], ['玉泉曹光彪西-503', '玉泉教7-304(多)'], '专业课', '1', '2', '2'],
                   ['软件工程管理', ['金波'], ['周一，7，8'], ['玉泉曹光彪西-503', '玉泉教7-304(多)'], '专业课', '1', '3', '3'],
                   ['计算机网络', ['陆魁军'], ['周一6，7，8'], ['玉泉曹光彪西-503', '玉泉教7-304(多)'], '专业课', '0', '4', ' 2'],
                   ['计算机网络', ['陆魁军'], ['周一，7，8'], ['玉泉曹光彪西-503', '玉泉教7-304(多)'], '专业课', '0', '5', '3'],
                   ['计算机网络', ['陆魁军'], ['周一，7，8'], ['玉泉曹光彪西-503', '玉泉教7-304(多)'], '专业课', '0', '6', '3'],
                   ['计算机网络', ['陆魁军'], ['周一6，7，8'], ['玉泉曹光彪西-503', '玉泉教7-304(多)'], '专业课', '0', '7', '5'], ]
    liuyanList = [['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                   '2017/12/12, 20:00:00', '1'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                   '2017/12/12, 20:00:00', '2'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '游客', '游客', '垃圾网站',
                   '2017/12/12, 20:00:00', '3'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '游客', '垃圾网站',
                   '2017/12/12, 20:00:00', '4'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                   '2017/12/12, 20:00:00', '5'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                   '2017/12/12, 20:00:00', '6'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '游客', '游客', '垃圾网站',
                   '2017/12/12, 20:00:00', '7'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '游客', '垃圾网站',
                   '2017/12/12, 20:00:00', '7'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                   '2017/12/12, 20:00:00', '9'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                   '2017/12/12, 20:00:00', '10'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '游客', '游客', '垃圾网站',
                   '2017/12/12, 20:00:00', '11'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '游客', '垃圾网站',
                   '2017/12/12, 20:00:00', '12'],
                  ]
    liuyanPage = Paginator(liuyanList, 10)
    liuyanPaginator = []
    for i in range(1, liuyanPage.num_pages + 1):
        for j in liuyanPage.page(i):
            tmp.append(liuyanPage.page(i))
        liuyanPaginator.append(tmp)
        tmp = []
    return render(request, 'student/index.html', {'GlobalNoticeList': GlobalNoticeList,
                                                  'unreadGlobalNotice': unreadGlobalNotice,
                                                  'CoursesList': CoursesList,
                                                  'liuyanPage': liuyanPage, 'liuyanPaginator': liuyanPaginator})


@user_passes_test(studentcheck, login_url="/login")
def course(request):
    tmp = []
    # 论坛贴子列表
    PostList = [['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                ['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                ['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                ['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                ['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                ['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                ['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                ['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                ['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                ['摸鱼求约', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                ['摸鱼', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                ['摸鱼', '邢卫', '2017/12/12, 20:00:00', '', '', '0'],
                ]
    PostPage = Paginator(PostList, 10)
    PostPaginator = []
    for i in range(1, PostPage.num_pages + 1):
        for j in PostPage.page(i):
            tmp.append(PostPage.page(i))
        PostPaginator.append(tmp)
        tmp = []
    # 通知列表设有一个标志位来标志是否已读，0为未读，1为已读，前端点击了通知详情按钮后，应该到后台将状态设置为已读
    NoticeList = [['1', '作业1已发布', '2017/12/12, 20:00:00', '作业1已发布，ddl为今晚10点'],
                  ['1', '作业2已发布', '2017/12/13, 20:00:00', '作业2已发布，ddl为今晚10点'],
                  ['0', '作业3已发布', '2017/12/14, 20:00:00', '作业3已发布，ddl为今晚10点'],
                  ['0', '作业4已发布', '2017/12/14, 20:00:00', '作业4已发布，ddl为今晚10点']]
    unreadNotice = 0
    for i in NoticeList:
        if i[0] == '0':
            unreadNotice += 1
    # 作业列表设有一个标志位来标志是否已提交，0为未提交，1为已提交，前端提交作业后，应该到后台将状态设置为已提交；
    # 应能正确指导前端进行页面跳转
    HwList = [['1', '作业1', '2017/12/12, 20:00:00'],
              ['1', '作业2', '2017/12/13, 20:00:00'],
              ['0', '作业3', '2017/12/14, 20:00:00']]
    unsubmitHw = 0
    for i in HwList:
        if i[0] == '0':
            unsubmitHw += 1
    # 教师信息表
    TeacherList = [['邢卫', '教授', '计算机科学与技术学院', '10086@zju.edu.cn', '18888888888'],
                   ['邢卫', '教授', '计算机科学与技术学院', '10086@zju.edu.cn', '18888888888'],
                   ]
    # 资源列表
    PPTList = [['uml.ppt', '刘玉生', '2017/12/12, 20:00:00'],
               ['5.ppt', '刘玉生', '2017/12/12, 20:00:00'],
               ['操作系统概念.ppt', '王泽杰', '2017/12/12, 20:00:00'],
               ['软件需求.ppt', '邢卫', '2017/12/12, 20:00:00'],
               ['作业成绩.ppt', '邢卫', '2017/12/12, 20:00:00'],
               ['uml.ppt', '刘生', '2017/12/12, 20:00:00'],
               ['5.ppt', '刘生', '2017/12/12, 20:00:00'],
               ['操作系统概念.ppt', '王泽杰', '2017/12/12, 20:00:00'],
               ['软件需求.ppt', '邢卫', '2017/12/12, 20:00:00'],
               ['作业成绩.ppt', '邢卫', '2017/12/12, 20:00:00']]
    PPTPage = Paginator(PPTList, 5)
    PPTPaginator = []
    for i in range(1, PPTPage.num_pages + 1):
        for j in PPTPage.page(i):
            tmp.append(PPTPage.page(i))
        PPTPaginator.append(tmp)
        tmp = []
    PDFList = [['uml.pdf', '刘玉生', '2017/12/12, 20:00:00'],
               ['5.pdf', '刘玉生', '2017/12/12, 20:00:00'],
               ['操作系统概念.pdf', '王泽杰', '2017/12/12, 20:00:00'],
               ['软件需求.pdf', '邢卫', '2017/12/12, 20:00:00'],
               ['作业成绩.pdf', '邢卫', '2017/12/12, 20:00:00'],
               ['作业成绩.pdf', '邢卫', '2017/12/12, 20:00:00']]
    PDFPage = Paginator(PDFList, 5)
    PDFPaginator = []
    for i in range(1, PDFPage.num_pages + 1):
        for j in PDFPage.page(i):
            tmp.append(PDFPage.page(i))
        PDFPaginator.append(tmp)
        tmp = []
    MediaList = [['uml.mp4', '刘玉生', '2017/12/12, 20:00:00'],
                 ['5.mp4', '刘玉生', '2017/12/12, 20:00:00'],
                 ['操作系统概念.mp4', '王泽杰', '2017/12/12, 20:00:00'],
                 ['软件需求.mp4', '邢卫', '2017/12/12, 20:00:00'],
                 ['作业成绩.mp4', '邢卫', '2017/12/12, 20:00:00']]
    MediaPage = Paginator(MediaList, 5)
    MediaPaginator = []
    for i in range(1, MediaPage.num_pages + 1):
        for j in MediaPage.page(i):
            tmp.append(MediaPage.page(i))
            MediaPaginator.append(tmp)
        tmp = []
    OthersList = [['uml.doc', '刘玉生', '2017/12/12, 20:00:00'],
                  ['5.docx', '刘玉生', '2017/12/12, 20:00:00'],
                  ['操作系统概念.doc', '王泽杰', '2017/12/12, 20:00:00'],
                  ['软件需求.xls', '邢卫', '2017/12/12, 20:00:00'],
                  ['作业成绩.docx', '邢卫', '2017/12/12, 20:00:00']]
    OthersPage = Paginator(OthersList, 5)
    OthersPaginator = []
    for i in range(1, OthersPage.num_pages + 1):
        for j in OthersPage.page(i):
            tmp.append(OthersPage.page(i))
            OthersPaginator.append(tmp)
        tmp = []
    return render(request, 'student/student_courses.html', {'PostList': PostList,
                                                            'PostPage': PostPage, 'PostPaginator': PostPaginator,
                                                            'NoticeList': NoticeList, 'unreadNotice': unreadNotice,
                                                            'HwList': HwList, 'unsubmitHw': unsubmitHw,
                                                            'TeacherList': TeacherList,
                                                            'PPTPage': PPTPage, 'PPTPaginator': PPTPaginator,
                                                            'PDFPage': PDFPage, 'PDFPaginator': PDFPaginator,
                                                            'MediaPage': MediaPage, 'MediaPaginator': MediaPaginator,
                                                            'OthersPage': OthersPage,
                                                            'OthersPaginator': OthersPaginator,
                                                            })


@user_passes_test(studentcheck, login_url="/login")
def hw(request):
    # 提交记录显示某次提交或保存的时间，保存为0，提交为1
    SubmitRecord = [['2017/12/12, 20:00:00', 0],
                    ['2017/12/13, 20:00:00', 0],
                    ['2017/12/14, 20:00:00', 1]]
    return render(request, 'student/student_hw.html', {'SubmitRecord': SubmitRecord})


@user_passes_test(studentcheck, login_url="/login")
def forum(request):
    tmp = []
    PostName = '摸鱼求约'  # 对应资源的名称
    PostList = [['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                 '2017/12/12, 20:00:00', '1'],
                ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                 '2017/12/12, 20:00:00', '2'],
                ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '游客', '游客', '垃圾网站',
                 '2017/12/12, 20:00:00', '3'],
                ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '游客', '垃圾网站',
                 '2017/12/12, 20:00:00', '4'],
                ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                 '2017/12/12, 20:00:00', '5'],
                ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                 '2017/12/12, 20:00:00', '6'],
                ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '游客', '游客', '垃圾网站',
                 '2017/12/12, 20:00:00', '7'],
                ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '游客', '垃圾网站',
                 '2017/12/12, 20:00:00', '7'],
                ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                 '2017/12/12, 20:00:00', '9'],
                ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                 '2017/12/12, 20:00:00', '10'],
                ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '游客', '游客', '垃圾网站',
                 '2017/12/12, 20:00:00', '11'],
                ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '游客', '垃圾网站',
                 '2017/12/12, 20:00:00', '12'],
                ]
    PostPage = Paginator(PostList, 10)
    PostPaginator = []
    for i in range(1, PostPage.num_pages + 1):
        for j in PostPage.page(i):
            tmp.append(PostPage.page(i))
        PostPaginator.append(tmp)
        tmp = []
    return render(request, 'student/student_forum.html', {'PostPage': PostPage,
                                                          'PostPaginator': PostPaginator,
                                                          'PostName': PostName})


@user_passes_test(studentcheck, login_url="/login")
def student_resource_comment(request):
    tmp = []
    ResourceName = 'uml.pdf'  #对应资源的名称
    CommentList = [['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                   '2017/12/12, 20:00:00', '1'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                   '2017/12/12, 20:00:00', '2'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '游客', '游客', '垃圾网站',
                   '2017/12/12, 20:00:00', '3'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '游客', '垃圾网站',
                   '2017/12/12, 20:00:00', '4'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                   '2017/12/12, 20:00:00', '5'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                   '2017/12/12, 20:00:00', '6'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '游客', '游客', '垃圾网站',
                   '2017/12/12, 20:00:00', '7'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '游客', '垃圾网站',
                   '2017/12/12, 20:00:00', '7'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                   '2017/12/12, 20:00:00', '9'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '教师', '垃圾网站',
                   '2017/12/12, 20:00:00', '10'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '游客', '游客', '垃圾网站',
                   '2017/12/12, 20:00:00', '11'],
                  ['/static/Semantic-UI-master/examples/assets/images/avatar/tom.jpg', '邢卫', '游客', '垃圾网站',
                   '2017/12/12, 20:00:00', '12'],
                  ]
    CommentPage = Paginator(CommentList, 10)
    CommentPaginator = []
    for i in range(1, CommentPage.num_pages + 1):
        for j in CommentPage.page(i):
            tmp.append(CommentPage.page(i))
        CommentPaginator.append(tmp)
        tmp = []
    return render(request, 'student/student_resource_comment.html', {'ResourceName': ResourceName,
                                                                     'CommentPage': CommentPage,
                                                                     'CommentPaginator': CommentPaginator})


@user_passes_test(studentcheck, login_url="/login")
def message(request):
    name = '吴朝晖'  #私信的对象
    History = [['/static/img/kk.png', '吴朝晖', '2017/12/12, 20:00:00', '网吧走起网吧走起网吧走起网吧走起网吧走起网吧走起网吧走起网吧走起网吧走起网吧走起网吧走起网吧走起网吧走起网吧走起'],
               ['/static/img/zju.jpg', '王泽杰', '2017/12/14, 20:00:00', '不去']]
    return render(request, 'student/message.html', {'name': name,
                                                    'History': History})


@user_passes_test(studentcheck, login_url="/login")
def ret(request):
    return render(request, 'tmp.html')


@user_passes_test(studentcheck, login_url="/login")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
