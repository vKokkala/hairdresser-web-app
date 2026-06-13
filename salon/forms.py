from django import forms
from .models import Appointment, AppointmentReport, Brand, Customer, Product, ProductType, Service


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "phone", "base_phone", "email", "notes"]


class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = ["name"]


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ["name"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["brand", "type", "size", "unit", "cost", "selling_price", "description", "notes"]


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "cost", "duration"]


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["date", "customer", "services", "duration"]
        widgets = {
            "date": forms.DateTimeInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            "services": forms.CheckboxSelectMultiple(),
        }


class ApointmentReportForm(forms.ModelForm):
    class Meta:
        model = AppointmentReport
        fields = ["notes", "duration"]
        