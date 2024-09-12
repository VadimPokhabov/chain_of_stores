from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response

from trading.models import Factory, Network, Businessman
from trading.serializers import (
    FactorySerializer,
    NetworkSerializer,
    BusinessmanSerializer,
)


class FactoryViewSet(viewsets.ModelViewSet):
    """
    Factory View Set
    """
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("country",)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data.copy()
        data.pop("arrears", None)
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class NetworkViewSet(viewsets.ModelViewSet):
    """
    Network View Set
    """
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class BusinessmanViewSet(viewsets.ModelViewSet):
    """
    Businessman View Set
    """
    queryset = Businessman.objects.all()
    serializer_class = BusinessmanSerializer
