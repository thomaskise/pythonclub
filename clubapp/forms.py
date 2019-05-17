from django import forms
from .models import Meeting, Resource

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'
        #can list individual fields seperated by a comma
        #also definition of form fields

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'
        #can list individual fields seperated by a comma
        #also definition of form fields