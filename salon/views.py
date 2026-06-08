from django.shortcuts import render

from salon.utils.views import crud_views

from .forms import BrandForm, CustomerForm, ProductForm, ProductTypeForm
from .models import Appointment, Brand, Customer, Product, ProductType


# utils
def home(request):
    return render(request, "salon/home.html")


CustomerList, CustomerDelete, CustomerCreate = crud_views(
    Customer,
    "customer",
    "customers",
    CustomerForm,
)

ProductTypeList, ProductTypeDelete, ProductTypeCreate = crud_views(
    ProductType,
    "product-type",
    "product_types",
    ProductTypeForm,
)

BrandList, BrandDelete, BrandCreate = crud_views(
    Brand,
    "brand",
    "brands",
    BrandForm,
)

ProductList, ProductDelete, ProductCreate = crud_views(
    Product, ProductForm, "product", "products"
)

AppointmentList, AppointmentDelete = crud_views(
    Appointment, "appointment", "appointments"
)
