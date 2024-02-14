from django.contrib import admin
from .models import Listing, MontUser

# admin.site.register(Listing)
# admin.site.register(MontUser)


@admin.register(MontUser)
class MontUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'dorm')
    ordering = ('first_name',)
    search_fields = ('first_name', 'last_name', 'dorm')


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    fields = (('title',), 'description', 'photo', 'price', 'condition', 'seller')
    list_display = ('title', 'price', 'seller')
    list_filter = ('price', 'condition')
    search_fields = ('title',)

