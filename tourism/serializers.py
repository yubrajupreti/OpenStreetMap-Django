from rest_framework import serializers
from .models import *



class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Hotel
        fields='__all__'


class GuestHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model= GuestHouse
        fields='__all__'


class MuseumSerializer(serializers.ModelSerializer):
    class Meta:
        model= Museum
        fields='__all__'


class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Attraction
        fields='__all__'


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Information
        fields='__all__'


class OutdoorActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model= OutdoorActivities
        fields='__all__'


class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Hostel
        fields='__all__'


class ThemeParkSerializer(serializers.ModelSerializer):
    class Meta:
        model= ThemePark
        fields='__all__'

class HotelRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=HotelRating
        fields='__all__'


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=HotelImage
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'