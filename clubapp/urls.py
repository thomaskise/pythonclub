from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('types/', views.gettypes, name='types'),
    path('resources/', views.getresources, name='resources'),
    path('meetings/', views.getmeetings, name='meetings'),
    path('meetingdetails/<int:id>', views.getmeetingdetails, name='meetingdetails'),
]