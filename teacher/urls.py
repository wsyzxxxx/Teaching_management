from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^teacher_courses', views.course, name='teacher_courses'),
    url(r'^teacher_hw', views.hw, name='teacher_hw'),
]