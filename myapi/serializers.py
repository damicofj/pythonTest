# API Serializers
from rest_framework import serializers
from myapi.models import Provider

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name', 'email', 'phone', 'language', 'currency']
        