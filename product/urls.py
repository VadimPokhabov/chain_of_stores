from django.urls import path, include
from rest_framework import routers

from product.apps import ProductConfig
from product.views import (
    FactoryProductViewSet,
    NetworkProductViewSet,
    BusinessmanProductViewSet,
)

app_name = ProductConfig.name

router = routers.DefaultRouter()
router.register(r"factory_product", FactoryProductViewSet)
router.register(r"network_product", NetworkProductViewSet)
router.register(r"businessman_product", BusinessmanProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
