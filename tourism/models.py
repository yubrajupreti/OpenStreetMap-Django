from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.



class Hotel(models.Model):
    name=models.CharField(max_length=255, unique=True)
    email=models.EmailField(max_length=255,null=True)
    phone=models.CharField(max_length=25,null=True)
    website=models.CharField(max_length=255, null=True)

class GuestHouse(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, null=True)
    phone = models.CharField(max_length=25, null=True)
    website = models.CharField(max_length=255, null=True)

class Museum(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, null=True)
    phone = models.CharField(max_length=25, null=True)
    website = models.CharField(max_length=255, null=True)


class Attraction(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, null=True)
    phone = models.CharField(max_length=25, null=True)
    website = models.CharField(max_length=255, null=True)


class Information(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, null=True)
    phone = models.CharField(max_length=25, null=True)
    website = models.CharField(max_length=255, null=True)


class OutdoorActivities(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, null=True)
    phone = models.CharField(max_length=25, null=True)
    website = models.CharField(max_length=255, null=True)


class Hostel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, null=True)
    phone = models.CharField(max_length=25, null=True)
    website = models.CharField(max_length=255, null=True)



class ThemePark(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, null=True)
    phone = models.CharField(max_length=25, null=True)
    website = models.CharField(max_length=255, null=True)



class HotelRating(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating=models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])

class HotelImage(models.Model):
    hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='hotel/image')


