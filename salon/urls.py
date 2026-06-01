from django.urls import path
from .views import CustomerCreateView, CustomerListView

urlpatterns = [
    path("", CustomerListView.as_view(), name="customer"),
    path("add-customer/", CustomerCreateView.as_view(), name="add-customer"),
]
