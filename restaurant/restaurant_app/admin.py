# restaurant_app/admin.py
from django.contrib import admin
from .models import Restaurant, MenuItem

admin.site.register(Restaurant)
admin.site.register(MenuItem)
