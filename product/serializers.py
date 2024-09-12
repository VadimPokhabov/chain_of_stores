from rest_framework import serializers
from product.models import FactoryProduct, NetworkProduct, BusinessmanProduct


class FactoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryProduct
        fields = "__all__"


class NetworkProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkProduct
        fields = "__all__"


class BusinessmanProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessmanProduct
        fields = "__all__"
