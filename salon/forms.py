from django import forms
from .models import Brand, Customer, Product, ProductType


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
