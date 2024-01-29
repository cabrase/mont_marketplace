from django.shortcuts import render
from datetime import datetime, timedelta


def home(request):
	name = "Carson"

	now = datetime.now()
	now = now - timedelta(hours=8)
	time = now.strftime('%I:%M %p PST')
	return render(request, 'listings/home.html', {
		"name": name,
		"time": time,
		})


def listings(request):
	now = datetime.now()
	now = now - timedelta(hours=8)
	time = now.strftime('%I:%M %p PST')
	return render(request, 'listings/listings.html', {
		"time": time,
		})
 