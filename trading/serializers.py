from rest_framework import serializers
from .models import Factory, Network, Businessman


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = "__all__"
        read_only_fields = ["arrears"]


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = "__all__"
        read_only_fields = ["arrears"]


class BusinessmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Businessman
        fields = "__all__"
        read_only_fields = ["arrears"]
