from django.shortcuts import render

from salon.utils.views import crud_views

from .forms import BrandForm, CustomerForm, ProductForm, ProductTypeForm
from .models import Appointment, Brand, Customer, Product, ProductType


# utils
def home(request):
    return render(request, "salon/home.html")


CustomerList, CustomerDelete, CustomerCreate = crud_views(
    Customer, CustomerForm, "customer", "customers"
)

ProductTypeList, ProductTypeDelete, ProductTypeCreate = crud_views(
    ProductType, ProductTypeForm, "product-type", "product_types"
)

BrandList, BrandDelete, BrandCreate = crud_views(Brand, BrandForm, "brand", "brands")

ProductList, ProductDelete, ProductCreate = crud_views(
    Product, ProductForm, "product", "products"
)

AppointmentList, AppointmentDelete = crud_views(
    Appointment, "appointment", "appointments"
)
