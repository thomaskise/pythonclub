from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('types/', views.gettypes, name='types'),
    path('resources/', views.getresources, name='resources'),
    path('meetings/', views.getmeetings, name='meetings'),
    path('meetingdetails/<int:id>', views.getmeetingdetails, name='meetingdetails'),
    path('newmeeting/', views.newmeeting, name='newmeeting'),
    path('newresource/', views.newresource, name='newresource'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]