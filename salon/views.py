from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.shortcuts import render

from .forms import BrandForm, CustomerForm, ProductForm, ProductTypeForm
from .models import Brand, Customer, Product, ProductType


def home(request):
    return render(request, "salon/home.html")

class CustomerListView(ListView):
    model = Customer
    template_name = "salon/customer_list.html"
    context_object_name = "customers"


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "salon/add_customer.html"
    success_url = reverse_lazy("customer")


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy("customer")


class ProductTypeListView(ListView):
    model = ProductType
    template_name = "salon/product_type_list.html"
    context_object_name = "product_types"


class ProductTypeCreateView(CreateView):
    model = ProductType
    form_class = ProductTypeForm
    template_name = "salon/add_product_type.html"
    success_url = reverse_lazy("product-type")


class BrandListView(ListView):
    model = Brand
    template_name = "salon/brand_list.html"
    context_object_name = "brands"


class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = "salon/add_brand.html"
    success_url = reverse_lazy("brand")


class BrandDeleteView(DeleteView):
    model = Brand
    success_url = reverse_lazy("brand")


class ProductListView(ListView):
    model = Product
    template_name = "salon/product_list.html"
    context_object_name = "products"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "salon/add_product.html"
    success_url = reverse_lazy("product")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("product")


class ProductTypeDeleteView(DeleteView):
    model = ProductType
    success_url = reverse_lazy("product-type")