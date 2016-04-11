from feasta.models import Session, Redemption, BulkRedemption
from django.utils.timezone import now, timedelta
def currentSession():
	session = Session.objects.filter(startdate__lte=now(), enddate__gte=now())
	if len(session) > 0:
		session = session[0]
	else:
		session = Session.objects.all()[-1]
		
	return session
	


def getSessionEndDays():
	days_left = (currentSession().enddate - now().date()).days
	return days_left
def populateNextDay(day):
	return day + timedelta(days=1)
def getDisabledDays(user):
	DATES = list()
	bulkreds = BulkRedemption.objects.filter(booked_by=user).filter(startdate__gte=now().date())
	reds = Redemption.objects.filter(booked_by=user).filter(date__gte=now().date()).order_by('-date')
	for b in bulkreds:
		currday =b.startdate
		while populateNextDay(currday) <= b.enddate:
			currday = populateNextDay(currday)
			DATES.append(currday)

	for r in reds:
		if len(Redemption.objects.filter(booked_by=user,date=r.date)) >= 3:
			DATES.append(r.date)
	Results = list()
	for DATE in DATES:
		d = DATE.day
		m = DATE.month
		y = DATE.year
		Results.append(str(y)+"-"+str(m)+"-"+str(d))
				 
	return Results

def getUserType(user):
	Result = "NA"
	if Student.objects.filter(user=user).exists():
		Result = "STUDENT"
	elif NonStudent.objects.filter(user=user).exists():	
		Result = "NONSTUDENT"

def getNotEaten(user):
	b=
	l=
	d=	
	return [b,l, d]