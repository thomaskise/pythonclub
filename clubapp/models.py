from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.TextField()
    

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'

class Minutes(models.Model):
    meeting=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    user=models.ManyToManyField(User)
    meetingminutes=models.TextField()

    def __str__(self):
        return self.meetingminutes
    
    class Meta:
        db_table='minutes'
        verbose_name_plural='minutes'

class ResourceType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.typename
    
    class Meta:
        db_table='resourcetype'
        verbose_name_plural='resourcetypes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.ForeignKey(ResourceType, on_delete=models.DO_NOTHING)
    # resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField(null=True, blank=True)
    resouceentrydate=models.DateField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedescription=models.TextField()

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.TextField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventtile
    
    class Meta:
        db_table='event'
        verbose_name_plural='events'