from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .forms import CustomerForm
from .models import Customer


class CustomerListView(ListView):
    model = Customer
    template_name = "salon/customer_list.html"
    context_object_name = "customers"


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "salon/add_customer.html"
    success_url = reverse_lazy("customer")
