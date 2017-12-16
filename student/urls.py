from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student_courses$', views.course, name='student_courses'),
    url(r'^student_hw', views.hw, name='student_hw'),
    url(r'^student_forum', views.forum, name='student_forum'),
]