from rest_framework import serializers
from .models import User, Room, Country, Province, City, Town, Order, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
	owner_rooms = serializers.HyperlinkedRelatedField(many=True, view_name='room-detail', read_only=True)
	user_order = serializers.HyperlinkedRelatedField(many=True, view_name='order-detail', read_only=True)
	user_comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)

	
	class Meta:
		model = User
		fields = ('url', 'openid','nickname', 'email', 'phone', 'photo', 'owner_rooms', 'user_order', 'user_comments')

class RoomSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
	country = serializers.ReadOnlyField(source='contry.countryname')
	province = serializers.ReadOnlyField(source='province.province')
	city = serializers.ReadOnlyField(source='city.cityname')
	town = serializers.ReadOnlyField(source='town.town')
	
	room_comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail',read_only=True)

	class Meta:
		model = Room
		fields = ('url', 'id', 'owner', 'price', 'description', 'publish', 'startTime', 'endTime', 'country', 'province', 'city', 'town', 'specificAddress', 'title', 'rating', 'room_comments')
		#'photo1', 'photo2','photo3','photo4','photo5','photo6','photo7','photo8','photo9',
class OrderSerializer(serializers.HyperlinkedModelSerializer):

	user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
	room = serializers.HyperlinkedRelatedField(view_name='room-detail', read_only=True)

	class Meta:
		model = Order
		fields = ('url', 'id', 'user', 'room', 'orderTime', 'arrivalData', 'departureData')

class CommentSerializer(serializers.HyperlinkedModelSerializer):

	user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
	room = serializers.HyperlinkedRelatedField(view_name='room-detail', read_only=True)

	class Meta:
		model = Comment
		fields = ('url', 'id', 'user', 'room', 'text', 'rating')

class CountrySearchRoomSerializer(serializers.HyperlinkedModelSerializer):
	
	#country_room = serializers.HyperlinkedRelatedField(many=True, view_name='room-country-detail', read_only=True)

	class Meta:
		model = Country
		fields = ('id', 'countryname')

class ProvinceSerializer(serializers.ModelSerializer):

	class Meta:
		model = Province
		fields = ('id', 'province', 'country')

class CitySerializer(serializers.ModelSerializer):

	class Meta:
		model = City
		fields = ('id', 'cityname', 'province')

class TownSerializer(serializers.ModelSerializer):

	class Meta:
		model = Town
		fields = ('id', 'town', 'city')




