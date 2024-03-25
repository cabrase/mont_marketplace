from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import Listing, MontUser
from django.contrib.auth.models import User
from .forms import ListingForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse

from django.contrib import messages


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
    if request.user.is_authenticated and request.user.montuser.email_is_verified is True:
        listing_data = Listing.objects.all()

        p = Paginator(Listing.objects.all().order_by('-created_at', '-updated_at'), 20)
        page = request.GET.get('page')
        posts = p.get_page(page)

        category = request.GET.get('category')

        if category:
            listing_data = listing_data.filter(category=category)

        return render(request, 'listings/listings.html', {
            'listing_data': listing_data,
            'posts': posts,
        })
    else:
        messages.success(request, "You aren't authorized to view this page.")
        return redirect('login')


def create_listing(request):
    if request.user.is_authenticated and request.user.montuser.email_is_verified is True:
        submitted = False
        if request.method == "POST":
            form = ListingForm(request.POST, request.FILES)
            if form.is_valid():
                listing = form.save(commit=False)
                listing.seller = request.user.id
                listing.save()
                return HttpResponseRedirect('/create_listing?submitted=True')
        else:
            form = ListingForm
            if 'submitted' in request.GET:
                submitted = True

        return render(request, 'listings/create_listing.html', {'form': form, 'submitted': submitted})
    else:
        messages.success(request, "You aren't authorized to view this page.")
        return redirect('login')


def my_listings(request):
    if request.user.is_authenticated and request.user.montuser.email_is_verified is True:
        me = request.user.id

        p = Paginator(Listing.objects.filter(seller=me).order_by('-created_at', '-updated_at'), 20)
        page = request.GET.get('page')
        my_posts = p.get_page(page)

        searched = request.POST.get('searched')
        if searched:
            my_posts = my_posts.filter(title__icontains=searched)
        return render(request, 'listings/my_listings.html', {
            'me': me,
            'my_posts': my_posts
        })

    else:
        messages.success(request, "You aren't authorized to view this page.")
        return redirect('login')


def show_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    listing_seller = User.objects.get(pk=listing.seller)
    return render(request, 'listings/show_listing.html', {
        'listing': listing,
        'listing_seller': listing_seller})


def update_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    form = ListingForm(request.POST or None, instance=listing)
    if form.is_valid():
        form.save()
        return redirect('show-listing', listing.id)
    return render(request, 'listings/update_listing.html',{
        'listing': listing,
        'form': form
    })


def search_listings(request):
    if request.method == "POST":
        searched = request.POST['searched']
        if searched:
            items = Listing.objects.filter(title__contains=searched)
            return render(request, 'listings/search_listings.html',
                          {'searched': searched,
                           'items': items
                           })
        else:
            return HttpResponseRedirect(reverse('listings'))


def filter_listings(request):
    category = request.GET.get('category')

    if category and category != 'All Categories':
        items = Listing.objects.filter(category=category)

        return render(request, 'listings/filter_listings.html', {
            'category': category,
            'items': items,
        })
    else:
        return HttpResponseRedirect(reverse('listings'))


def delete_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    listing.delete()
    messages.success(request, "Post Deleted")
    return redirect('listings')
