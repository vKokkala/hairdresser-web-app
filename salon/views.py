from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.shortcuts import render

from .forms import BrandForm, CustomerForm, ProductForm, ProductTypeForm
from .models import AppointmentReport, Brand, Customer, Product, ProductType


def home(request):
    return render(request, "salon/home.html")

class CustomerListView(ListView):
    model = Customer
    template_name = "salon/customer/list.html"
    context_object_name = "customers"


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "salon/customer/add.html"
    success_url = reverse_lazy("customer")


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy("customer")


class ProductTypeListView(ListView):
    model = ProductType
    template_name = "salon/product_type/list.html"
    context_object_name = "product_types"


class ProductTypeCreateView(CreateView):
    model = ProductType
    form_class = ProductTypeForm
    template_name = "salon/product_type/add.html"
    success_url = reverse_lazy("product-type")


class BrandListView(ListView):
    model = Brand
    template_name = "salon/brand/list.html"
    context_object_name = "brands"


class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = "salon/brand/add.html"
    success_url = reverse_lazy("brand")


class BrandDeleteView(DeleteView):
    model = Brand
    success_url = reverse_lazy("brand")


class ProductListView(ListView):
    model = Product
    template_name = "salon/product/list.html"
    context_object_name = "products"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "salon/product/add.html"
    success_url = reverse_lazy("product")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("product")


class ProductTypeDeleteView(DeleteView):
    model = ProductType
    success_url = reverse_lazy("product-type")


# class AppointmentReportListView(CreateView):
#     model = AppointmentReport
#     template_name = "salon/"