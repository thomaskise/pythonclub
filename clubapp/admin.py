from django.contrib import admin
from .models import Meeting, Minutes, ResourceType, Resource, Event

# Register your models here.
admin.site.register(Meeting)
admin.site.register(Minutes)
admin.site.register(ResourceType)
admin.site.register(Resource)
admin.site.register(Event)