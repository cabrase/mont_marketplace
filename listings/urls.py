from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('listings', views.listings, name="listings"),
    path('create_listing', views.create_listing, name='create-listing'),
    path('listings/<listing_id>', views.show_listing, name='show-listing'),
    path('search_listings', views.search_listings, name='search-listings'),
    path('update_listing/<listing_id>', views.update_listing, name='update-listing'),
    path('delete_listing/<listing_id>', views.delete_listing, name='delete-listing'),
]
