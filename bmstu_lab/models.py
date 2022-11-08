from django.db import models


class Cars(models.Model):
    id = models.IntegerField(primary_key=True)
    car = models.CharField(max_length=30)
    dicription = models.CharField(max_length=255)
    price = models.CharField(max_length=30)


    class Meta:
        managed = False
        db_table = 'cars'

class Tx(models.Model):
    id_TX = models.IntegerField(primary_key=True)
    avto = models.CharField(max_length=30)
    power = models.CharField(max_length=30)
    drive_unit = models.CharField(max_length=30)
    max_speed = models.CharField(max_length=30)
    acceleration = models.CharField(max_length=30)


    class Meta:
        managed = False
        db_table = 'tx'


class User(models.Model):
    id_user = models.IntegerField(primary_key=True)
    FIO = models.CharField(max_length=30)
    birthday = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    e_mail = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'user'

class Arenda(models.Model):
    id_arenda = models.IntegerField(primary_key=True)
    avtoarenda = models.CharField(max_length=30)
    payment = models.CharField(max_length=30)
    day = models.CharField(max_length=30)
    month = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    timearenda = models.DateTimeField(auto_now=True, verbose_name="Когда последний раз была в аренде?")

    class Meta:
        managed = False
        db_table = 'arenda'


