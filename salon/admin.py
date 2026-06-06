from django.contrib import admin

from .models import (
    AppointmentReportService,
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


@admin.register(AppointmentReport)
class AppointmentReportAdmin(admin.ModelAdmin):
    list_display = ["duration", "get_customer", "get_date"]

    def get_customer(self, obj):
        return obj.appointment.customer

    def get_date(self, obj):
        return obj.appointment.date

    get_customer.short_description = "Customer"
    get_date.short_description = "Date"


admin.site.register([Product, Brand, ProductType, AppointmentReportService])
