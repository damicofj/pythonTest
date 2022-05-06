# API Serializers
from rest_framework import serializers
from myapi.models import Provider
from myapi.models import ServiceArea

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name', 'email', 'phone', 'language', 'currency']
        
class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ['name', 'price', 'geo']
        
