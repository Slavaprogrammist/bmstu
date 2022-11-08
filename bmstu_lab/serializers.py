
from bmstu_lab.models import Cars, User, Arenda, Tx
from rest_framework import serializers


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ["id", "car", "dicription", "price"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id_user", "FIO", "birthday", "phone", "e_mail"]

class ArendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arenda
        fields = ["id_arenda", "avtoarenda", "payment", "day", "month", "year", "timearenda"]

class TxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tx
        fields = ["id_TX", "avto", "power", "drive_unit", "max_speed", "acceleration"]
