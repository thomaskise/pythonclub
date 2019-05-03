from django.shortcuts import render, get_object_or_404
from .models import Meeting, Minutes, Resource, Event, User

# Create your views here.
def index (request):
    return render(request, 'clubapp/index.html')

def getresources(request):
    resource_list=Resource.objects.all()
    return render(request, 'clubapp/resources.html' ,{'resource_list' : resource_list})

def getmeetings(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'clubapp/meetings.html', {'meetings_list': meetings_list})

def meetingdetails(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    minutescount=Minutes.objects.filter(meeting=id).count()
    minutes=Minutes.objects.filter(meeting=id)
    # minutes=Minutes.objects.filter(meeting=id)
    # meeting=get_object_or_404(Meeting, pk=id)
    context={
        'meet' : meeting,
        'mincount' : minutescount,
        'minutes' : minutes,
    }
    return render(request, 'clubapp/meetingdetails.html', context=context)