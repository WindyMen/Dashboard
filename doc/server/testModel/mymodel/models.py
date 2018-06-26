
from django.db import models
from django.utils import timezone

# Create your models here.

'''
rm -f tmp.db db.sqlite3
rm -r mymodel/migration
'''

class User(models.Model):
	openid = models.CharField(primary_key=True, max_length=32)
	nickname = models.CharField(max_length=32, null=True)
	email = models.CharField(max_length=32, null=True)
	phone = models.CharField(max_length=32, null=True)
	photo = models.CharField(max_length=200, null=True)


class Country(models.Model):
	countryname = models.CharField(max_length=32, default="")

	def __str__(self):
		return self.countryname

class Province(models.Model):
	province = models.CharField(max_length=32, default="")
	country = models.ForeignKey(Country, related_name='country_province', on_delete=models.CASCADE)

	def __str__(self):
		return self.province

class City(models.Model):
	cityname = models.CharField(max_length=32, default="")
	province = models.ForeignKey(Province, related_name='province_city', on_delete=models.CASCADE)

	def __str__(self):
		return self.cityname

class Town(models.Model):
	town = models.CharField(max_length=32, default="")
	city = models.ForeignKey(City, related_name='city_town', on_delete=models.CASCADE)

	def __str__(self):
		return self.town

class Room(models.Model):
	owner = models.ForeignKey(User, related_name='owner_rooms', on_delete=models.CASCADE, null=True)
	#roomName = models.CharField(max_length=32)
	#roomType = models.CharField(max_length=32)
	description = models.TextField(max_length=100, null=True)
	price = models.DecimalField(max_digits=16, decimal_places=2, default=0, null=True)
	publish = models.DateTimeField(default=timezone.now, null=True)
	startTime = models.DateTimeField(null=True)
	endTime = models.DateTimeField(null=True)
	#numOfPerson = models.IntegerField()
	#numOfBed = models.IntegerField()
	#numOfBathroom = models.IntegerField()
	contry = models.ForeignKey(Country, related_name='country_room', on_delete=models.CASCADE, null=True)
	province = models.ForeignKey(Province, related_name='province_room', on_delete=models.CASCADE, null=True)
	city = models.ForeignKey(City, related_name='city_room', on_delete=models.CASCADE, null=True)
	town = models.ForeignKey(Town, related_name='town_room', on_delete=models.CASCADE, null=True)
	specificAddress = models.CharField(max_length=60, null=True)
	#otherOption = models.CharField(max_length=32, default=None)
	title = models.CharField(max_length=32, null=True)
	#photo1 = models.ImageField(upload_to='room/', blank=True, null=True)
	#photo2 = models.ImageField(upload_to='room/', blank=True, null=True)
	#photo3 = models.ImageField(upload_to='room/', blank=True, null=True)
	#photo4 = models.ImageField(upload_to='room/', blank=True, null=True)
	#photo5 = models.ImageField(upload_to='room/', blank=True, null=True)
	#photo6 = models.ImageField(upload_to='room/', blank=True, null=True)
	#photo7 = models.ImageField(upload_to='room/', blank=True, null=True)
	#photo8 = models.ImageField(upload_to='room/', blank=True, null=True)
	#photo9 = models.ImageField(upload_to='room/', blank=True, null=True)
	rating = models.IntegerField(null=True)

	def __str__(self):
		return 'owner:{}, title:{}'.format(self.owner, self.title)

class RoomPhoto(models.Model):
	room = models.ForeignKey(Room, related_name='room_photo', on_delete=models.CASCADE, null=True)
	photo = models.ImageField(upload_to='room/', blank=True, null=True)

class Comment(models.Model):
	user = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE, null=True)
	room = models.ForeignKey(Room, related_name='room_comments', on_delete=models.CASCADE, null=True)
	text = models.TextField()
	rating = models.IntegerField()

class CommentPhoto(models.Model):
	comment = models.ForeignKey(Comment, related_name='comment_photo', on_delete=models.CASCADE, null=True)
	photo = models.ImageField(upload_to='comments/', blank=True, null=True)



class Order(models.Model):
	orderTime = models.DateTimeField(default=timezone.now, null=True)
	user = models.ForeignKey(User, related_name='user_order', on_delete=models.CASCADE, null=True)
	room = models.ForeignKey(Room, related_name='room_order', on_delete=models.CASCADE, null=True)
	arrivalData = models.DateTimeField(null=True)
	departureData = models.DateTimeField(null=True)
