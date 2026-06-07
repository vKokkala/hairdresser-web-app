from django.shortcuts import render

from salon.utils.views import crud_views

from .forms import BrandForm, CustomerForm, ProductForm, ProductTypeForm
from .models import Brand, Customer, Product, ProductType


# utils
def home(request):
    return render(request, "salon/home.html")


CustomerList, CustomerCreate, CustomerDelete = crud_views(
    Customer, CustomerForm, "customer", "customers"
)
ProductTypeList, ProductTypeCreate, ProductTypeDelete = crud_views(
    ProductType, ProductTypeForm, "product-type", "product_types"
)
BrandList, BrandCreate, BrandDelete = crud_views(Brand, BrandForm, "brand", "brands")
ProductList, ProductCreate, ProductDelete = crud_views(
    Product, ProductForm, "product", "products"
)
