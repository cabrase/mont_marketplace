from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import Listing, User, MontUser
from .forms import ListingForm
from django.http import HttpResponseRedirect


def home(request):
    name = User.objects.all()
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
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create_listing?submitted=True')
    else:
        form = ListingForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'listings/create_listing.html', {'form': form, 'submitted': submitted})


def show_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    return render(request, 'listings/show_listing.html', {'listing': listing})


def update_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    form = ListingForm(request.POST or None, instance=listing)
    if form.is_valid():
        form.save()
        return redirect('show-listing', listing.id)
    return render(request, 'listings/update_listing.html',
                  {'listing': listing,
                   'form': form})


def search_listings(request):
    if request.method == "POST":
        searched = request.POST['searched']
        items = Listing.objects.filter(title__contains=searched)
        return render(request, 'listings/search_listings.html',
                      {'searched': searched,
                       'items': items})
    else:
        return render(request, 'listings/search_listings.html',
                      {})
