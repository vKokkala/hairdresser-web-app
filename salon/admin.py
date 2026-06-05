from django.contrib import admin

from .models import (
    Customer,
    Product,
    ProductType,
    Brand,
    Service,
    Appointment,
    AppointmentReport,
)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone"]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "cost"]


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["customer", "date", "duration", "get_services"]

    def get_services(self, obj):
        return ", ".join(obj.services.values_list("name", flat=True))

    get_services.short_description = "Services"


admin.site.register([Product, Brand, ProductType, AppointmentReport])
