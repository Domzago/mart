from django.contrib import admin
from .models import Item

# Register your models here.

admin.site.site_header = 'Zago Mart'
admin.site.site_title = 'Welcome to the mart'
admin.site.index_title = 'This is the place'

admin.site.register(Item)