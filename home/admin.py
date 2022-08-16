from django.contrib import admin

# Register your models here.
from .models import Users, Booking

admin.site.register(Users)
admin.site.register(Booking)
# admin.site.register(Profile)