import json
import requests
import pandas as pd

from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import *


def fetch_data(sector):
    """
    type = df['tourism']
    filter_category = type.unique()
    category=['hotel','guest_house','museum','attraction','information','Outdoor_Activities','hostel','theme_park']
    """
    request = requests.get(
        'https://overpass-api.de/api/interpreter?data=%2F*%0AThis%20has%20been%20generated%20by%20the%20overpass-turbo%20wizard.'
        '%0AThe%20original%20search%20was%3A%0A%E2%80%9C%28historic%3D%20*%20%20%20or%20tourism%3D%20*%20%29%20in%20kathmandu%E2%80%9D%0A*%2F%0A%5Bout%3Ajson%5D%5Btimeout%3A25%5D%3B%0A%2F%2F%20fetch%20area%20%E2%80%9Ckathmandu%E2%80%9D%20to%20search%20in%0Aarea%28id%3A3604583125%29-%3E.searchArea%3B%0A%2F%2F%20gather%20results%0A%28%0A%20%20%2F%2F%20query%20part%20for%3A%20%E2%80%9Chistoric%3D*%E2%80%9D%0A%20%20node%5B%22historic%22%5D%28area.searchArea%29%3B%0A%20%20way%5B%22historic%22%5D%28area.searchArea%29%3B%0A%20%20relation%5B%22historic%22%5D%28area.searchArea%29%3B%0A%20%20%2F%2F%20query%20part%20for%3A%20%E2%80%9Ctourism%3D*%E2%80%9D%0A%20%20node%5B%22tourism%22%5D%28area.searchArea%29%3B%0A%20%20way%5B%22tourism%22%5D%28area.searchArea%29%3B%0A%20%20relation%5B%22tourism%22%5D%28area.searchArea%29%3B%0A%29%3B%0A%2F%2F%20print%20results%0Aout%20body%3B%0A%3E%3B%0Aout%20skel%20qt%3B')
    data = request.json()['elements']
    tag_list = []
    for tag in data:
        for key, value in tag.items():
            if key == 'tags':
                tag_list.append(value)

    df = pd.DataFrame(tag_list)
    filt = (df['tourism'] == sector)
    categ_data = df.loc[filt, ['name', 'email', 'phone', 'website']]
    null_sep_filt = (categ_data['name'].isnull() == True)
    filt_data = categ_data.loc[~null_sep_filt]
    if len(filt_data)>10:
        remaining_data=filt_data[0:10]
    else:
        remaining_data=filt_data

    json_string=remaining_data.to_json(orient='records')
    return json.loads(json_string)


class HotelView(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    @action(methods=['get'], detail=False)
    def fetch(self,request):
        """
            get_or_create the instance of hotel

        """
        data=fetch_data('hotel')
        hotel_list=[]

        for hotel in data:

            try:
                single_hotel=Hotel.objects.get(name=hotel['name'])
                hotel_list.append(single_hotel)

            except Hotel.DoesNotExist:
                hotel_obj=Hotel(name=hotel['name'], email=hotel['email'], phone=hotel['phone'], website=hotel['website'])
                hotel_obj.save()
                hotel_list.append(hotel_obj)

        serializers=HotelSerializer(hotel_list,many=True)
        return Response(serializers.data)


class GuestHouseView(ModelViewSet):
    queryset = GuestHouse.objects.all()
    serializer_class = GuestHouseSerializer

    @action(methods=['get'], detail=False, permission_classes=[AllowAny])
    def fetch(self, request):
        """
            get_or_create the instance of guest house

        """
        data = fetch_data('guest_house')
        guest_house_list = []

        for guest in data:

            try:
                single_guest_house = GuestHouse.objects.get(name=guest['name'])
                guest_house_list.append(single_guest_house)

            except GuestHouse.DoesNotExist:
                guest_obj = GuestHouse(name=guest['name'], email=guest['email'], phone=guest['phone'],
                                  website=guest['website'])
                guest_obj.save()
                guest_house_list.append(guest_obj)

        serializers = GuestHouseSerializer(guest_house_list, many=True)
        return Response(serializers.data)


class MuseumView(ModelViewSet):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer

    @action(methods=['get'], detail=False, permission_classes=[AllowAny])
    def fetch(self, request):
        """
            get_or_create the instance of museum

        """
        data = fetch_data('museum')
        museum_list = []

        for museum in data:

            try:
                single_museum = Museum.objects.get(name=museum['name'])
                museum_list.append(single_museum)

            except Museum.DoesNotExist:
                museum_obj = Museum(name=museum['name'], email=museum['email'], phone=museum['phone'],
                                  website=museum['website'])
                museum_obj.save()
                museum_list.append(museum_obj)

        serializers = MuseumSerializer(museum_list, many=True)
        return Response(serializers.data)


class AttractionView(ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer

    @action(methods=['get'], detail=False, permission_classes=[AllowAny])
    def fetch(self, request):
        """
            get_or_create the instance of attraction

        """
        data = fetch_data('attraction')
        attraction_list = []

        for attraction in data:

            try:
                single_attraction = Attraction.objects.get(name=attraction['name'])
                attraction_list.append(single_attraction)

            except Attraction.DoesNotExist:
                attraction_obj = Attraction(name=attraction['name'], email=attraction['email'], phone=attraction['phone'],
                                    website=attraction['website'])
                attraction_obj.save()
                attraction_list.append(attraction_obj)

        serializers = AttractionSerializer(attraction_list, many=True)
        return Response(serializers.data)


class InformationView(ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer

    @action(methods=['get'], detail=False, permission_classes=[AllowAny])
    def fetch(self, request):
        """
            get_or_create the instance of information

        """
        data = fetch_data('information')
        information_list = []

        for information in data:

            try:
                single_information = Information.objects.get(name=information['name'])
                information_list.append(single_information)

            except Information.DoesNotExist:
                information_obj = Information(name=information['name'], email=information['email'], phone=information['phone'],
                                    website=information['website'])
                information_obj.save()
                information_list.append(information_obj)

        serializers = InformationSerializer(information_list, many=True)
        return Response(serializers.data)


class OutDoorActivitiesView(ModelViewSet):
    queryset = OutdoorActivities.objects.all()
    serializer_class = OutdoorActivitiesSerializer

    @action(methods=['get'], detail=False, permission_classes=[AllowAny])
    def fetch(self, request):
        """
            get_or_create the instance of outdoor_activities

        """
        data = fetch_data('Outdoor_Activities')
        outdoor_activities_list = []

        for outdoor_activities in data:

            try:
                single_outdoor_activities = OutdoorActivities.objects.get(name=outdoor_activities['name'])
                outdoor_activities_list.append(single_outdoor_activities)

            except OutdoorActivities.DoesNotExist:
                outdoor_activities_obj = OutdoorActivities(name=outdoor_activities['name'], email=outdoor_activities['email'], phone=outdoor_activities['phone'],
                                    website=outdoor_activities['website'])
                outdoor_activities_obj.save()
                outdoor_activities_list.append(outdoor_activities_obj)

        serializers = OutdoorActivitiesSerializer(outdoor_activities_list, many=True)
        return Response(serializers.data)


class HostelView(ModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer

    @action(methods=['get'], detail=False, permission_classes=[AllowAny])
    def fetch(self, request):
        """
            get_or_create the instance of hotel

        """
        data = fetch_data('hostel')
        hostel_list = []

        for hostel in data:

            try:
                single_hostel = Hostel.objects.get(name=hostel['name'])
                hostel_list.append(single_hostel)

            except Hostel.DoesNotExist:
                hostel_obj = Hostel(name=hostel['name'], email=hostel['email'], phone=hostel['phone'],
                                    website=hostel['website'])
                hostel_obj.save()
                hostel_list.append(hostel_obj)

        serializers = HostelSerializer(hostel_list, many=True)

        return Response(serializers.data)


class ThemeParkView(ModelViewSet):
    queryset = ThemePark.objects.all()
    serializer_class = ThemeParkSerializer

    @action(methods=['get'], detail=False, permission_classes=[AllowAny])
    def fetch(self, request):
        """
            get_or_create the instance of hotel

        """
        data = fetch_data('theme_park')
        theme_park_list = []

        for theme_park in data:
            try:

                single_theme_park = ThemePark.objects.get(name=theme_park['name'])
                theme_park_list.append(single_theme_park)

            except ThemePark.DoesNotExist:
                theme_park_obj = ThemePark(name=theme_park['name'], email=theme_park['email'], phone=theme_park['phone'],
                                    website=theme_park['website'])
                theme_park_obj.save()
                theme_park_list.append(theme_park_obj)

        serializers = ThemeParkSerializer(theme_park_list, many=True)
        return Response(serializers.data)


class HotelRatingView(ModelViewSet):
    queryset = HotelRating.objects.all()
    serializer_class = HotelRatingSerializer


class HotelImageView(ModelViewSet):
    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializer


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



