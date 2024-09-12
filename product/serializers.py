from rest_framework import serializers
from product.models import FactoryProduct, NetworkProduct, BusinessmanProduct


class FactoryProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор Factory Product
    """
    class Meta:
        model = FactoryProduct
        fields = "__all__"


class NetworkProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор Network Product
    """
    class Meta:
        model = NetworkProduct
        fields = "__all__"


class BusinessmanProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор Businessman Product
    """
    class Meta:
        model = BusinessmanProduct
        fields = "__all__"
