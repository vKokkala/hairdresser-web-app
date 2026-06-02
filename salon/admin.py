from django.contrib import admin

from .models import Customer, Product, ProductType, Brand


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone"]


admin.site.register([Product, Brand, ProductType])
