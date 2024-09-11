from django.contrib import admin

from product.models import FactoryProduct, NetworkProduct, BusinessmanProduct


@admin.register(FactoryProduct)
class FactoryProductAdmin(admin.ModelAdmin):
    pass


@admin.register(NetworkProduct)
class NetworkProductAdmin(admin.ModelAdmin):
    pass


@admin.register(BusinessmanProduct)
class BusinessmanProductAdmin(admin.ModelAdmin):
    pass
