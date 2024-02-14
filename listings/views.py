from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Listing
from .forms import ListingForm
from django.http import HttpResponseRedirect


def home(request):
	name = "Carson"

	now = datetime.now()
	now = now - timedelta(hours=8)
	time = now.strftime('%I:%M %p PST')
	return render(request, 'listings/home.html', {
		'name': name,
		'time': time,
		})


def listings(request):
	listing_data = Listing.objects.all()
	now = datetime.now()
	now = now - timedelta(hours=8)
	time = now.strftime('%I:%M %p PST')
	return render(request, 'listings/listings.html', {
		'time': time,
		'listing_data': listing_data
		})


def create_listing(request):
	submitted = False
	if request.method == "POST":
		form = ListingForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/create_listing?submitted=True')
	else:
		form = ListingForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'listings/create_listing.html', {'form': form, 'submitted': submitted})
