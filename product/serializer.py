from rest_framework import serializers
from product.models import *



class productMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = productMain
        fields = '__all__'


class productImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = productImage
        fields = '__all__'