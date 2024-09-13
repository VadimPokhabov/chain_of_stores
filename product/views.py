from rest_framework import viewsets

from product.models import FactoryProduct, NetworkProduct, BusinessmanProduct
from product.serializers import (
    FactoryProductSerializer,
    NetworkProductSerializer,
    BusinessmanProductSerializer,
)


class FactoryProductViewSet(viewsets.ModelViewSet):
    """
    Factory Product View Set
    """
    queryset = FactoryProduct.objects.all()
    serializer_class = FactoryProductSerializer


class NetworkProductViewSet(viewsets.ModelViewSet):
    """
    Network Product View Set
    """
    queryset = NetworkProduct.objects.all()
    serializer_class = NetworkProductSerializer


class BusinessmanProductViewSet(viewsets.ModelViewSet):
    """
    Network Product View Set
    """
    queryset = BusinessmanProduct.objects.all()
    serializer_class = BusinessmanProductSerializer
