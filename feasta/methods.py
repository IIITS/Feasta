from feasta.models import Session, Redemption, BulkRedemption, Student, NonStudent, Meal
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

def getNextMeal(day,meal):
	
	NEXT_MEAL={
		'BF':'L',
		'L':'D',
		'D':'BF'
	}
	NEXT_DAY = {
		'BF':day,
		'L':day,
		'D':day + timedelta(days=1)
	}
 	return [NEXT_DAY[str(meal)], NEXT_MEAL[str(meal)]]

def getUserType(user):
	Result = "NA"
	if Student.objects.filter(user=user).exists():
		Result = "STUDENT"
	elif NonStudent.objects.filter(user=user).exists():	
		Result = "NONSTUDENT"
	return Result	

def getNotEaten(user):
	s = currentSession()
	bulk_ne = BulkRedemption.objects.filter(booked_by=user).filter(startdate__gte=s.startdate)
	ne = Redemption.objects.filter(booked_by=user).filter(date__gte=s.startdate)
	BNE_N = []
	LNE_N = []
	DNE_N = []
	TOT = []
	for entry in bulk_ne:
		date = entry.startdate
		meal = entry.startmeal
		while date <= entry.enddate:

				if meal == "BF":
					BNE_N.append({"date":date,"meal":meal})
				elif meal == "L":
					LNE_N.append({"date":date,"meal":meal})
				elif meal == "D":
					DNE_N.append({"date":date,"meal":meal})
				print meal
				TOT.append({"date":date,"meal":meal})	
				r = getNextMeal(date, meal)
				date = r[0]
				meal = r[1]

	for entry in ne:
		meal = entry.meal
		date = entry.date
		if meal == "BF":
			BNE_N.append({"date":date,"meal":meal})
		elif meal == "L":
			LNE_N.append({"date":date,"meal":meal})
		elif meal == "D":
			DNE_N.append({"date":date,"meal":meal})
		print meal
		TOT.append({"date":date,"meal":meal})	
	return [BNE_N,LNE_N, DNE_N,TOT]