from rest_framework import serializers
from accounts.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class User_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Profile
        fields = '__all__'


class login_topSerializer(serializers.ModelSerializer):
    class Meta:
        model = login_top
        fields = '__all__'


class UserCartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCartProduct
        fields = '__all__'


class UserCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCart
        fields = '__all__'


