from rest_framework import viewsets

from product.models import FactoryProduct, NetworkProduct, BusinessmanProduct
from product.serializers import (
    FactoryProductSerializer,
    NetworkProductSerializer,
    BusinessmanProductSerializer,
)


class FactoryProductViewSet(viewsets.ModelViewSet):
    queryset = FactoryProduct.objects.all()
    serializer_class = FactoryProductSerializer


class NetworkProductViewSet(viewsets.ModelViewSet):
    queryset = NetworkProduct.objects.all()
    serializer_class = NetworkProductSerializer


class BusinessmanProductViewSet(viewsets.ModelViewSet):
    queryset = BusinessmanProduct.objects.all()
    serializer_class = BusinessmanProductSerializer
