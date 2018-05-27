from django.contrib import admin
from api.models import *

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('name','advertiser')

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Advertiser)
admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(User)
