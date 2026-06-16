from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from salon.utils.view_utils import crud_views

from .forms import (
    ApointmentReportForm,
    AppointmentForm,
    AppointmentReportServiceForm,
    BrandForm,
    CustomerForm,
    ProductForm,
    ProductTypeForm,
    ServiceForm,
)
from .models import (
    Appointment,
    AppointmentReport,
    AppointmentReportService,
    Brand,
    Customer,
    Product,
    ProductType,
    Service,
)


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

BaseAppointmentList, AppointmentDelete, AppointmentCreate, BaseAppointmentUpdate = (
    crud_views(Appointment, "appointment", "appointments", AppointmentForm)
)


class AppointmentList(BaseAppointmentList):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["upcoming"] = Appointment.objects.filter(date__gte=now).order_by("date")
        context["past"] = Appointment.objects.filter(date__lt=now).order_by("-date")
        return context


def _make_service_formset(extra=0):
    return modelformset_factory(
        AppointmentReportService,
        form=AppointmentReportServiceForm,
        extra=extra,
        can_delete=True,
    )


class AppointmentUpdate(BaseAppointmentUpdate):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        appointment = self.object

        try:
            report = AppointmentReport.objects.get(appointment=appointment)
            report_form = ApointmentReportForm(instance=report)
            ServiceFormSet = _make_service_formset()
            service_formset = ServiceFormSet(
                queryset=report.report_service.all(), prefix="services"
            )
        except AppointmentReport.DoesNotExist:
            report = None
            report_form = ApointmentReportForm()
            initial = [
                {"service": s.pk, "duration": s.duration, "cost": s.cost}
                for s in appointment.services.all()
            ]
            ServiceFormSet = _make_service_formset(extra=len(initial))
            service_formset = ServiceFormSet(
                queryset=AppointmentReportService.objects.none(),
                initial=initial,
                prefix="services",
            )

        context["appointment_report"] = report
        context["appointment_report_form"] = report_form
        context["service_formset"] = service_formset
        return context

    def form_valid(self, form):
        self.object = form.save()
        appointment = self.object

        if appointment.status == "done":
            report, _ = AppointmentReport.objects.get_or_create(appointment=appointment)

            report_form = ApointmentReportForm(self.request.POST, instance=report)
            if report_form.is_valid():
                report_form.save()

            ServiceFormSet = _make_service_formset()
            service_formset = ServiceFormSet(
                self.request.POST,
                queryset=report.report_service.all(),
                prefix="services",
            )
            if service_formset.is_valid():
                instances = service_formset.save(commit=False)
                for instance in instances:
                    instance.appointment_report = report
                    instance.save()
                for obj in service_formset.deleted_objects:
                    obj.delete()

        return HttpResponseRedirect(self.get_success_url())


ServiceList, ServiceDelete, ServiceCreate, ServiceUpdate = crud_views(
    Service, "service", "services", ServiceForm
)


def customer_appointment_history(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    appointments = (
        Appointment.objects.filter(customer=customer)
        .order_by("-date")
        .prefetch_related("report", "services")
    )
    now = timezone.now()
    past_appointments = appointments.filter(date__lt=now)
    future_appointments = appointments.filter(date__gte=now)
    return render(
        request,
        "salon/customer_appointment_history.html",
        {
            "customer": customer,
            "past_appointments": past_appointments,
            "future_appointments": future_appointments,
        },
    )
