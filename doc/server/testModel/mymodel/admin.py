from django.contrib import admin
from .models import User, Room, Comment, Order, Country, City, Province, Town, RoomPhoto

# Register your models here.

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Comment)
admin.site.register(Order)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Province)
admin.site.register(Town)
admin.site.register(RoomPhoto)