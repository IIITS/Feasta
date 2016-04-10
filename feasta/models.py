from __future__ import unicode_literals
from django.db.models import *
from django.contrib.auth.models import User
from django.utils.timezone import now
from feasta.config import model_choices

class Application(Model):
	name = CharField(max_length=50) 
	title = TextField(default='Feasta | Mess @ IIITS')

class UserEntity(Model):
	user = OneToOneField(User)
	permissions = TextField(default='NA')
	is_admin = BooleanField(default=False)

class Session(Model):
	name = CharField(max_length=50)
	year = CharField( max_length=4, choices=model_choices['YEAR_CHOICES'], default=now().year)
	startdate = DateField(auto_now=False, auto_now_add=False) 
	enddate = DateField(auto_now=False, auto_now_add=False)
	class Meta:
		unique_together = (("year","name"), ("startdate","enddate"))
class Meal(Model):
	name = CharField(max_length=50, choices=model_choices['MEAL'])
	starttime = TimeField(auto_now=False, auto_now_add=False)
	endtime = TimeField(auto_now=False, auto_now_add=False)

class Mess(Model):
	name = CharField(max_length=50)
	vendors = TextField(default='NA')
	description = TextField(default='NA')
class Menu(Model):
	mess=ForeignKey(Mess,on_delete=CASCADE)
	meal = ForeignKey(Meal,on_delete=CASCADE)
	day = CharField(max_length=20, choices=model_choices['WEEK_DAY'])
	items = TextField(default='NA')	
class Vendor(Model):
	name = CharField(max_length=50)
	description = TextField(default='NA')
class Student(UserEntity,Model):
	rollno = CharField(max_length=20)
	batch = CharField(max_length=20, choices=model_choices['BATCH'])
	branch = CharField(max_length=20, choices=model_choices['BRANCH'])
	default_mess = ForeignKey(Mess)
class NonStudent(UserEntity,Model):		
	nstype = CharField(max_length=20, choices=model_choices['NON_STUDENT_TYPE'])
	

class BulkRedemption(Model):
	booked_by=ForeignKey(User)
	booked_time=DateTimeField(auto_now_add=True)
	startdate = DateField(editable=True)
	enddate = DateField(editable=True)
	startmeal = ForeignKey(Meal, related_name='startmeal')
	endmeal = ForeignKey(Meal, related_name = 'endmeal')
	class Meta:
		unique_together = (("booked_by","startdate","enddate"))
class Redemption(Model):
	booked_by = ForeignKey(User)
	booked_time = DateTimeField(auto_now_add=True)
	meal = ForeignKey(Meal)
	date = DateField(db_index=True)
	class Meta:
		unique_together = (("booked_by","date","meal"))
		index_together = (("date","meal"),("booked_by","meal"),("booked_by","date"))