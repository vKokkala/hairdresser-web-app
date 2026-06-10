from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from salon.utils.view_utils import crud_views

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

BaseAppointmentList, AppointmentDelete, AppointmentCreate, AppointmentUpdate = crud_views(
    Appointment, "appointment", "appointments", AppointmentForm
)

class AppointmentList(BaseAppointmentList):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["upcoming"] = Appointment.objects.filter(date__gte=now).order_by("date")
        context["past"] = Appointment.objects.filter(date__lt=now).order_by("-date")
        return context

ServiceList, ServiceDelete, ServiceCreate, ServiceUpdate = crud_views(
    Service, "service", "services", ServiceForm
)


def customer_appointment_history(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    appointments = Appointment.objects.filter(customer=customer).order_by("-date")
    return render(request, "salon/customer_appointment_history.html", {
        "customer": customer,
        "appointments": appointments,
    })
