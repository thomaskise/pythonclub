from django.test import TestCase
from .models import Meeting, Minutes, ResourceType, Resource, Event
from .views import index, gettypes, getresources, getmeetings, getmeetingdetails
from .forms import MeetingForm, ResourceForm
from django.urls import reverse
from django.contrib.auth.models import User
import datetime

# Test Tables.
class MeetingTest(TestCase):
   def test_string(self):
      meeting = Meeting(meetingtitle="first meeting")
      self.assertEqual(str(meeting), meeting.meetingtitle)

   def test_string(self):
      meeting = Meeting(meetingagenda="This is what the meeting is about")
      self.assertEqual(str(meeting), meeting.meetingtitle)

   def test_table(self):
      self.assertEqual(str(Meeting._meta.db_table), 'meeting')
   
class MinutesTest(TestCase):
   def test_string(self):
      minutes = Minutes(meetingminutes="These are the minutes")
      self.assertEqual(str(minutes), minutes.meetingminutes)

   def test_table(self):
      self.assertEqual(str(Minutes._meta.db_table), 'minutes')

class ResourceTypeTest(TestCase):
   def test_string(self):
       type=ResourceType(typename="Video")
       self.assertEqual(str(type), type.typename)

   def test_table(self):
       self.assertEqual(str(ResourceType._meta.db_table), 'resourcetype')

class ResourceTest(TestCase):
   def test_string(self):
      resource = Resource(resourcename="Data Projector")
      self.assertEqual(str(resource), resource.resourcename)

   def test_table(self):
      self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
   def test_string(self):
      event = Event(eventtitle="Python Club Meetup")
      self.assertEqual(str(event), event.eventtitle)

   def test_table(self):
      self.assertEqual(str(Event._meta.db_table), 'event')

#Test URL/Views
class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
      response = self.client.get(reverse('index'))
      self.assertEqual(response.status_code, 200)

class GetTypesTest(TestCase):
   def test_view_url_accessible_by_name(self):
      response = self.client.get(reverse('types'))
      self.assertEqual(response.status_code, 200)

class GetMeetingsTest(TestCase):
   def test_view_url_accessible_by_name(self):
      response = self.client.get(reverse('meetings'))
      self.assertEqual(response.status_code, 200)

class GetMeetingDetailsTest(TestCase):
   def setUp(self):
      self.u1=User.objects.create(username='myuser1')
      self.u2=User.objects.create(username='myuser2')
      self.meeting=Meeting.objects.create(meetingtitle='first meeting',
      meetingdate='2019-05-12', meetingtime='10:00am',
      meetinglocation='school', meetingagenda='Learn Python')
      self.min1=Minutes.objects.create(meeting=self.meeting )
      self.min1.user.add(self.u1)
      self.min1.user.add(self.u2)

   def test_meeting_detail_success(self):
      response = self.client.get(reverse('meetingdetails', args=(self.meeting.id,)))
      self.assertEqual(response.status_code, 200)

#Other tests
class ResourceMoreTest(TestCase):
   #set up one time sample data
   def setup(self):
      self.type = ResourceType(typename = 'Video')
      self.resource = Resource(resourcename = 'Projector', 
      resourcetype = self.type, resouceentrydate = '2019-05-08')
   
   def test_string(self):
      resource = self.setup()
      self.assertEqual(str(self.resource), self.resource.resourcename)

   def test_type(self):
      resource = self.setup()
      self.assertEqual(self.resource.resourcetype, self.type)
      
   def test_date(self):
      resource = self.setup()
      self.assertEqual(self.resource.resouceentrydate, '2019-05-08')

#form tests
class NewMeetingsFormTest(TestCase):
   def test_form_new_meeting(self):
      title = 'meeting title test data'
      date = '2019-05-31'
      time = '10:00:00'
      location = 'tba'
      agenda = 'agenda'
      form_data = {'meetingtitle': title, 'meetingdate': date, 'meetingtime': time,
      'meetinglocation': location, 'meetingagenda': agenda}
      form = MeetingForm(data=form_data)
      self.assertTrue(form.is_valid())

class Setup_Class(TestCase):

   def setUp(self):
      self.u=User.objects.create(username='myuser')
      self.type = ResourceType(typename = 'Video')
      self.resource = Resource.objects.create(
      resourcename="This is the resource name", 
      resourcetype="self.type", resourceentrydate="2019-05-16", 
      user="me", resourcedescription="description")
      self.resource1=Resource.objects.create(resource=self.resource )
      self.resource1.user.add(self.u)

class Resource_Form_Test(TestCase):
   def setUp(self):
      self.u=User.objects.create(username='myuser')
      self.type = ResourceType(typename = 'Video')
      self.resource = Resource.objects.create(
      resourcename="This is the resource name", 
      resourcetype="self.type", resourceentrydate="2019-05-16", 
      user="me", resourcedescription="description")
      self.resource1=Resource.objects.create(resource=self.resource )
      self.resource1.user.add(self.u)
   # Valid Form Data
   def test_ResourceForm_valid(self):
      form = ResourceForm(formdata=self.resource1)
      self.assertTrue(form.is_valid())

class Resource_Form_Test(TestCase):
   def setUp(self):
      self.u=User.objects.create(username='duck2000')
      self.type = ResourceType.objects.create(typename = 'Video')
      resourcename="Resource Name"
      resourcetype=self.type
      resourceurl='https://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python'
      resouceentrydate=datetime.date(2020, 5, 17)
      user=self.u
      resourcedescription="description"
      self.form_data = {'resourcename':resourcename,
      'resourcetype':self.type,
      'resourceurl':resourceurl,
      'resouceentrydate':resouceentrydate,
      'user':self.u,'resourcedescription':resourcedescription}
      print(resourcename)
      print(resourcetype)
      print(resourceurl)
      print(resouceentrydate)
      print(user)
      print(resourcedescription)

   # Valid Form Data
   def test_ResourceForm_valid(self):
      form = ResourceForm(data=self.form_data)
      print(self.form_data)
      self.assertTrue(form.is_valid())
