from django.urls import path, include
from rest_framework import routers

from trading.apps import TradingConfig
from trading.views import FactoryViewSet, NetworkViewSet, BusinessmanViewSet

app_name = TradingConfig.name


router = routers.DefaultRouter()
router.register(r'factory', FactoryViewSet)
router.register(r'network', NetworkViewSet)
router.register(r'businessman', BusinessmanViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
