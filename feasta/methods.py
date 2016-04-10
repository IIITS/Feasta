from feasta.models import Session
from django.utils.timezone import now
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