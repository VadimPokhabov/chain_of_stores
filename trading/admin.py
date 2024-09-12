from django.contrib import admin

from trading.models import Factory, Network, Businessman


def clear_debt(modeladmin, request, queryset):
    for obj in queryset:
        obj.arrears = 0
        obj.save()


clear_debt.short_description = "Очистить задолженность"

fields_display = [
    "name",
    "email",
    "country",
    "city",
    "street",
    "house_number",
    "arrears",
    "supplier",
    "create_time",
]


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "country",
        "city",
        "street",
        "house_number",
        "arrears",
        "create_time",
    ]
    list_filter = ("city",)
    actions = [clear_debt]


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = fields_display
    list_filter = ("city",)
    actions = [clear_debt]


@admin.register(Businessman)
class BusinessmanAdmin(admin.ModelAdmin):
    list_display = fields_display
    list_filter = ("city",)
    actions = [clear_debt]
