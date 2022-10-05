from django.db import models

# Create your models here.

class Accommodation(models.Model):
    acc_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=30)
    contacts = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'accommodation'

class Guest(models.Model):
    guest_name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'guests'

class Booking(models.Model):
    guest_id = models.IntegerField()
    accommodation_id = models.IntegerField()
    dates = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'bookings'