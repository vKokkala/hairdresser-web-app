from django.urls import path

from .views import (
    AppointmentCreate,
    AppointmentDelete,
    AppointmentList,
    AppointmentUpdate,
    BrandCreate,
    BrandDelete,
    BrandList,
    BrandUpdate,
    CustomerCreate,
    CustomerDelete,
    CustomerList,
    CustomerUpdate,
    ProductCreate,
    ProductDelete,
    ProductList,
    ProductTypeCreate,
    ProductTypeDelete,
    ProductTypeList,
    ProductTypeUpdate,
    ProductUpdate,
    ServiceCreate,
    ServiceDelete,
    ServiceList,
    ServiceUpdate,
    customer_appointment_history,
    home,
)

urlpatterns = [
    path("", home, name="home"),
    # Customer
    path("customer/", CustomerList.as_view(), name="customer"),
    path("customer/add", CustomerCreate.as_view(), name="add-customer"),
    path("customer/<int:pk>/edit/", CustomerUpdate.as_view(), name="edit-customer"),
    path("customer/<int:pk>/delete/", CustomerDelete.as_view(), name="delete-customer"),
    path("customer/<int:pk>/history/", customer_appointment_history, name="customer-history"),
    # Product types
    path("product-types/", ProductTypeList.as_view(), name="product-type"),
    path("product-types/add/", ProductTypeCreate.as_view(), name="add-product-type"),
    path("product-types/<int:pk>/edit/", ProductTypeUpdate.as_view(), name="edit-product-type"),
    path(
        "product-types/<int:pk>/delete/",
        ProductTypeDelete.as_view(),
        name="delete-product-type",
    ),
    # Brands
    path("brands/", BrandList.as_view(), name="brand"),
    path("brands/add/", BrandCreate.as_view(), name="add-brand"),
    path("brands/<int:pk>/edit/", BrandUpdate.as_view(), name="edit-brand"),
    path("brands/<int:pk>/delete/", BrandDelete.as_view(), name="delete-brand"),
    # Products
    path("products/", ProductList.as_view(), name="product"),
    path("products/add/", ProductCreate.as_view(), name="add-product"),
    path("products/<int:pk>/edit/", ProductUpdate.as_view(), name="edit-product"),
    path("products/<int:pk>/delete/", ProductDelete.as_view(), name="delete-product"),
    # Appointments
    path("appointments/", AppointmentList.as_view(), name="appointment"),
    path("apppointment/add/", AppointmentCreate.as_view(), name="add-appointment"),
    path("appointments/<int:pk>/edit/", AppointmentUpdate.as_view(), name="edit-appointment"),
    path(
        "appointments/<int:pk>/delete/",
        AppointmentDelete.as_view(),
        name="delete-appointment",
    ),
    # Services
    path("services/", ServiceList.as_view(), name="service"),
    path("services/add/", ServiceCreate.as_view(), name="add-service"),
    path("services/<int:pk>/edit/", ServiceUpdate.as_view(), name="edit-service"),
    path("services/<int:pk>/delete/", ServiceDelete.as_view(), name="delete-service"),
]
