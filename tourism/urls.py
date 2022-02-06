from django.urls import path, include

from rest_framework import routers


from .views import *

router=routers.DefaultRouter()
router.register('user', UserView, basename='user')
router.register('hotel', HotelView, basename='hotel')
router.register('hotelrating', HotelRatingView, basename='hotelrating')
router.register('hotelimage', HotelImageView, basename='hotelimage')
router.register('guesthouse', GuestHouseView, basename='guesthouse')
router.register('museum', MuseumView, basename='museun')
router.register('attraction', AttractionView, basename='attraction')
router.register('information', InformationView, basename='information')
router.register('outdoor', OutDoorActivitiesView, basename='outdoor')
router.register('hostel', HostelView, basename='hostel')
router.register('themepark', ThemeParkView, basename='themepark')


urlpatterns = [

	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework)')),


]