from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
	path('', views.api_root),
	path('user/', views.UserList.as_view(), name='user-list'),
	#path('user/', views.user_list, name='user-list'),
	path('user/<pk>/', views.UserDetail.as_view(), name='user-detail'),
	#path('user/<pk>/comments/', views.user_comment, name='user-comment'),
	#path('user/<pk>/orders/', views.user_order, name='user-order'),

	path('room/', views.RoomList.as_view(), name='room-list'),
	path('room/<pk>/', views.RoomDetail.as_view(), name='room-detail'),
	#path('room/<pk>/comments/', views.room_comment, name='room-comment'),

	path('country/', views.CountryList.as_view(), name='country-list'),
	path('country/<pk>/', views.CountryDetail.as_view(), name='country-detail'),
	path('country/<pk>/rooms/', views.country_room, name='room-country-list'),

	path('province/', views.ProvinceList.as_view(), name='province-list'),
	path('province/<pk>/', views.ProvinceDetail.as_view(), name='province-detail'),
	path('province/<pk>/rooms/', views.province_room, name='room-province-list'),

	path('city/', views.CityList.as_view(), name='city-list'),
	path('city/<pk>/', views.CityDetail.as_view(), name='city-detail'),
	#path('city/<city>/rooms/', views.city_room, name='room-city-list'),

	path('town/', views.TownList.as_view(), name='town-list'),
	path('town/<pk>/', views.TownDetail.as_view(), name='town-detail'),
	path('town/<pk>/rooms/', views.town_room, name='room-town-list'),

	path('order/', views.OrderList.as_view(), name='order-list'),
	path('order/<pk>/', views.OrderDetail.as_view(), name='order-detail'),

	path('comment/', views.CommentList.as_view(), name='comment-list'),
	path('comment/<pk>/', views.CommentDetail.as_view(), name='comment-detail'),
#	path('comment/<pk>/comments', views.comment_list, name='room-comment'),

	path('session/', views.Wxlogin, name='login'),
	path('searchRoomByCity/', views.searchRoomByCity, name='search-room-by-city'),
	path('searchRoom/', views.searchRoom, name='search-room'),
	path('saveRoomPhoto/', views.saveRoomPhoto, name='save-room-photo'),
	path('getRoomPhoto/', views.getRoomPhoto, name='get-room-photo'),
	path('saveCommentPhoto/', views.saveCommentPhoto, name='save-comment-photo'),
	path('getCommentPhoto/', views.getCommentPhoto, name='get-comment-photo'),
])