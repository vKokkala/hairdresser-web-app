from django.urls import path
from .views import (
    BrandCreateView,
    BrandDeleteView,
    BrandListView,
    CustomerCreateView,
    CustomerDeleteView,
    CustomerListView,
    ProductCreateView,
    ProductDeleteView,
    ProductListView,
    ProductTypeCreateView,
    ProductTypeDeleteView,
    ProductTypeListView,
    home,
)

# TODO: too much repetition. Can I make smth generic?
urlpatterns = [
    path("", home, name="home"),
    # Customer
    path("customer/", CustomerListView.as_view(), name="customer"),
    path("customer/add", CustomerCreateView.as_view(), name="add-customer"),
    path("customer/<int:pk>/delete/", CustomerDeleteView.as_view(), name="delete-customer"),
    # Product types
    path("product-types/", ProductTypeListView.as_view(), name="product-type"),
    path("product-types/add/", ProductTypeCreateView.as_view(), name="add-product-type"),
    path("product-types/<int:pk>/delete/", ProductTypeDeleteView.as_view(), name="delete-product-type"),
    # Brands
    path("brands/", BrandListView.as_view(), name="brand"),
    path("brands/add/", BrandCreateView.as_view(), name="add-brand"),
    path("brands/<int:pk>/delete/", BrandDeleteView.as_view(), name="delete-brand"),
    # Products
    path("products/", ProductListView.as_view(), name="product"),
    path("products/add/", ProductCreateView.as_view(), name="add-product"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="delete-product"),
]
