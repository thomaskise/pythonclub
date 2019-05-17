from django.shortcuts import render, get_object_or_404
from .models import Meeting, Minutes,ResourceType, Resource, Event, User
from .forms import MeetingForm, ResourceForm

# Create your views here.
def index (request):
    return render(request, 'clubapp/index.html')

def gettypes(request):
    type_list=ResourceType.objects.all()
    return render(request, 'clubapp/types.html')

def getresources(request):
    resource_list=Resource.objects.all()
    return render(request, 'clubapp/resources.html' ,{'resource_list' : resource_list})

def getmeetings(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'clubapp/meetings.html', {'meetings_list': meetings_list})

def getmeetingdetails(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    minutescount=Minutes.objects.filter(meeting=id).count()
    minutes=Minutes.objects.filter(meeting=id)
    context={
        'meet' : meeting,
        'mincount' : minutescount,
        'minutes' : minutes,
    }
    return render(request, 'clubapp/meetingdetails.html', context=context)

def newmeeting(request):
    form=MeetingForm
    if request.method =='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm() #not required. redisplays empty form
    else: 
        form=MeetingForm()
    return render(request, 'clubapp/newmeeting.html', {'form' : form})

def newresource(request):
    form=ResourceForm
    if request.method =='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm() #not required. redisplays empty form
    else: 
        form=ResourceForm()
    return render(request, 'clubapp/newresource.html', {'form' : form})