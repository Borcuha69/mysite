from django.contrib import admin
from .models import *

# Register your models here.
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['name',]
    search_fields = ['name', 'email', 'id']

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)