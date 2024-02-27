from django.contrib import admin
from .models import Listing

# admin.site.register(Listing)
# admin.site.register(MontUser)


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    fields = (('title',), 'description', 'photo', 'price', 'condition', 'seller')
    list_display = ('title', 'price', 'seller')
    list_filter = ('price', 'condition')
    search_fields = ('title',)

