from django.urls import path
from .views import (
    BrandCreateView,
    BrandListView,
    CustomerCreateView,
    CustomerListView,
    ProductCreateView,
    ProductListView,
    ProductTypeCreateView,
    ProductTypeListView,
    home,
)

urlpatterns = [
    path("", home, name="home"),
    path("customer/", CustomerListView.as_view(), name="customer"),
    path("customer/add", CustomerCreateView.as_view(), name="add-customer"),
    path("product-types/", ProductTypeListView.as_view(), name="product-type"),
    path("product-types/add/", ProductTypeCreateView.as_view(), name="add-product-type"),
    path("brands/", BrandListView.as_view(), name="brand"),
    path("brands/add/", BrandCreateView.as_view(), name="add-brand"),
    path("products/", ProductListView.as_view(), name="product"),
    path("products/add/", ProductCreateView.as_view(), name="add-product"),
]
