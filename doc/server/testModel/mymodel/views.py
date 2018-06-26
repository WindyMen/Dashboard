from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from .models import User, Room, Country, Province, City, Town, Order, Comment, RoomPhoto, CommentPhoto
from .serializers import UserSerializer, RoomSerializer, CountrySearchRoomSerializer, ProvinceSerializer, CitySerializer, TownSerializer, OrderSerializer, CommentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrReadOnly
from django.core.files.base import ContentFile
import urllib.request as ulb
import json
import datetime

# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
	return Response({
			'users':reverse('user-list', request=request, format=format),
			'rooms':reverse('room-list', request=request, format=format),
			'countrys':reverse('country-list', request=request, format=format),
			'provinces':reverse('province-list', request=request, format=format),
			'citys':reverse('city-list', request=request, format=format),
			'towns':reverse('town-list', request=request, format=format),
			'orders':reverse('order-list', request=request, format=format),
			'comments':reverse('comment-list', request=request, format=format),
		})
'''
@api_view(['GET', 'POST'])
def user_list(request, format=None):
	if request.method == 'GET':
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_BAD_REQUEST)
'''

#列出信息没问题，创建用户没问题，
class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class RoomList(generics.ListCreateAPIView):
	queryset = Room.objects.all()
	serializer_class = RoomSerializer

	def perform_create(self, serializer):
		data = self.request.data
		
		user = User.objects.get(openid=data['owner'])
		#country = Country.objects.get(countryname=data['country'])
		#province = Province.objects.get(province=data['province'])
		city = City.objects.get(cityname=data['city'])
		#town = Town.objects.get(town=data['town'])

		serializer.save(owner=user, city=city)

class OrderList(generics.ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def perform_create(self, serializer):
		data = self.request.data
		user = User.objects.get(openid=data['user'])
		room = Room.objects.get(pk=data['room'])

		serializer.save(user=user, room=room)

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

class CommentList(generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

	def perform_create(self, serializer):
		data = self.request.data
		user = User.objects.get(openid=data['user'])
		room = Room.objects.get(pk=data['room'])

		serializer.save(user=user, room=room)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer



class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Room.objects.all()
	serializer_class = RoomSerializer


class CountryList(generics.ListCreateAPIView):
	queryset = Country.objects.all()
	serializer_class = CountrySearchRoomSerializer


class CityList(generics.ListAPIView):
	queryset = City.objects.all()
	serializer_class = CitySerializer



class CountryDetail(generics.RetrieveAPIView):
	queryset = Country.objects.all()
	serializer_class = CountrySearchRoomSerializer

class ProvinceList(generics.ListAPIView):
	queryset = Province.objects.all()
	serializer_class = ProvinceSerializer

class ProvinceDetail(generics.RetrieveAPIView):
	queryset = Province.objects.all()
	serializer_class = ProvinceSerializer


class CityDetail(generics.RetrieveAPIView):
	queryset = City.objects.all()
	serializer_class = CitySerializer

class TownList(generics.ListAPIView):
	queryset = Town.objects.all()
	serializer_class = TownSerializer

class TownDetail(generics.RetrieveAPIView):
	queryset = Town.objects.all()
	serializer_class = TownSerializer


@api_view(['GET'])
def country_room(request, pk, format=None):

	try:
		country = Country.objects.get(pk=pk)
	except Country.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		rooms = country.country_room
		serializer = RoomSerializer(rooms, context={'request':request}, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def province_room(request, pk, format=None):
	try:
		province = Province.objects.get(pk=pk)
	except Province.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		rooms = province.province_room
		serializer = RoomSerializer(rooms, context={'request':request}, many=True)
		return Response(serializer.data)

'''
@api_view(['GET'])
def city_room(request, pk, format=None):

	try:
		city = City.objects.get(cityname=city)
	except City.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		rooms = city.city_room
		serializer = RoomSerializer(rooms, context={'request':request}, many=True)
		return Response(serializer.data)
'''

@api_view(['GET'])
def town_room(request, pk, format=None):
	try:
		town = Town.objects.get(pk=pk)
	except Town.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		rooms = town.town_room
		serializer = RoomSerializer(rooms, context={'request':request}, many=True)
		return sResponse(serializer.data)

#{"session_key":"RWrMGg\/P+pcj02OlRT26bw==","openid":"o_yAE5qCnd1N-XccUf6HFudpr-Is"}
def Wxlogin(request):
	res = {}
	if request.method == 'POST':
		url = "https://api.weixin.qq.com/sns/jscode2session?appid=wx1fc7283d72fb0be8&secret=1b52397140e7b75ae54f48df83b8481a&js_code="
		code = request.POST.get("code")
		url = url + code + '&grant_type=authorization_code'
		with ulb.urlopen(url) as response:
			result = response.read()
		#对user进行检验

		result = result.decode()
		res = {
			'result': result
		}
		res = json.dumps(res)

		#openid的处理
		result = result.split(':')
		temp = result[1].split(',')
		session_key = temp[0][1:len(temp[0]) - 1]
		openid = result[2][1:len(result[2]) - 2]
		try:
			user = User.objects.get(pk=openid)

		except User.DoesNotExist:
			nickname = request.POST.get('nickName')
			photo = request.POST.get('photo')
			user = User.objects.create(openid=openid, nickname=nickname, photo=photo)
			
		return HttpResponse(res, content_type="application/json")

	#return json.dumps(res)

def searchRoom(request):
	result = []
	if request.method == 'POST':
		cityname = request.POST.get("cityname")
		date_from_year = request.POST.get("date_from_year")
		date_from_month = request.POST.get("date_from_month")
		date_from_day = request.POST.get("date_from_day")
		date_to_year = request.POST.get("date_to_year")
		date_to_month = request.POST.get("date_to_month")
		date_to_day = request.POST.get("date_to_day")
		date_from = datetime.datetime(int(date_from_year), int(date_from_month), int(date_from_day), 0, 0)
		date_to = datetime.datetime(int(date_to_year), int(date_to_month), int(date_to_day), 0, 0)
		try:
			city = City.objects.get(cityname=cityname)
			rooms = city.city_room.filter(startTime__lte=date_from, endTime__gte=date_to)
			for i in range(rooms.count()):
				result.append({"id":rooms[i].id, "title": rooms[i].title, "price": str(rooms[i].price), "portrait": rooms[i].owner.photo})
			
			res = json.dumps(result)
			return HttpResponse(res, content_type="application/json")
			

		except City.DoesNotExist:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)

def searchRoomByCity(request):
	result = []
	if request.method == 'POST':
		cityname = request.POST.get("cityname")
		try:
			city = City.objects.get(cityname=cityname)
			rooms = city.city_room.all()
			for i in range(rooms.count()):
				result.append({"id":rooms[i].id, "title": rooms[i].title, "price": str(rooms[i].price), "portrait": rooms[i].owner.photo})
			
			res = json.dumps(result)
			return HttpResponse(res, content_type="application/json")
		except City.DoesNotExist:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)

def saveRoomPhoto(request):
	if request.method == 'POST':
		room_id = request.POST.get("room_id")
		photo_file = ContentFile(request.FILES["file"].read())
		if photo_file is None:
			return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
		try:
			room = Room.objects.get(pk=room_id)			
			try:
				photo = RoomPhoto.objects.create(room=room)
				photo.photo.save(request.FILES['file'].name, photo_file)
				return HttpResponse(status=status.HTTP_201_CREATED)
			except Exception:
				return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

		except Room.DoesNotExist:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)


def getRoomPhoto(request):
	if request.method == 'POST':
		room_id = request.POST.get("room_id")
		try:
			room = Room.objects.get(pk=room_id)
			try:
				res = []
				photos = room.room_photo.all()
				for i in range(0, photos.count()):
					photo = photos[i].photo.name
					photo = "https://windymen.mynatapp.cc/image/" + photo
					result = {
						"photo": photo
					}
					res.append(result)
				return HttpResponse(json.dumps(res), content_type="application/json")
			except Exception:
				return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

		except Room.DoesNotExist:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)

def saveCommentPhoto(request):
	if request.method == 'POST':
		comment_id = request.POST.get('comment_id')
		photo_file = ContentFile(request.FILES["file"].read())
		if photo_file is None:
			return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
		try:
			comment = Comment.objects.get(pk=comment_id)
			try:
				photo = CommentPhoto.objects.create(comment=comment)
				photo.photo.save(request.FILES['file'].name, photo_file)
				return HttpResponse(status=status.HTTP_201_CREATED)
			except Exception:
				return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
		except Comment.DoesNotExist:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)

def getCommentPhoto(request):
	if request.method == 'POST':
		comment_id = request.POST.get('comment_id')
		try:
			comment = Comment.objects.get(pk=comment_id)

			try:
				res = []
				photos = comment.photo.all()
				for i in range(0, photos.count()):
					photo = photos[i].photo.name
					photo = "https://windymen.mynatapp.cc/image/" + photo
					result = {
						"photo": photo
					}
					res.append(result)
				return HttpResponse(json.dumps(res), content_type="application/json")
			except Exception:
				return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
		except Comment.DoesNotExist:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)

'''
@api_view(['GET'])
def user_comment(request, pk, format=None):
	try:
		user = User.objects.get(pk=pk)
	except User.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		comments = user.user_comments
		serializer = CommentSerializer(comments, context={'request':request}, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def user_order(request, pk, format=None):
	try:
		user = User.objects.get(pk=pk)
	except User.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		orders = user.user_order
		serializer = OrderSerializer(orders, context={'request':request}, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def room_comment(request, pk, format=None):
	try:
		room = Room.objects.get(pk=pk)
	except Room.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		comments = room.room_comments
		serializer = CommentSerializer(comments, context={'request':request}, many=True)
		return Response(serializer.data)
'''