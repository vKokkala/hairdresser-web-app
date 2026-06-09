from django.shortcuts import render

from salon.utils.views import crud_views

from .forms import AppointmentForm, BrandForm, CustomerForm, ProductForm, ProductTypeForm, ServiceForm
from .models import Appointment, Brand, Customer, Product, ProductType, Service


# utils
def home(request):
    return render(request, "salon/home.html")


CustomerList, CustomerDelete, CustomerCreate, CustomerUpdate = crud_views(
    Customer,
    "customer",
    "customers",
    CustomerForm,
)

ProductTypeList, ProductTypeDelete, ProductTypeCreate, ProductTypeUpdate = crud_views(
    ProductType,
    "product-type",
    "product_types",
    ProductTypeForm,
)

BrandList, BrandDelete, BrandCreate, BrandUpdate = crud_views(
    Brand,
    "brand",
    "brands",
    BrandForm,
)

ProductList, ProductDelete, ProductCreate, ProductUpdate = crud_views(
    Product, "product", "products", ProductForm
)

AppointmentList, AppointmentDelete, AppointmentCreate, AppointmentUpdate = crud_views(
    Appointment, "appointment", "appointments", AppointmentForm
)

ServiceList, ServiceDelete, ServiceCreate, ServiceUpdate = crud_views(
    Service, "service", "services", ServiceForm
)
