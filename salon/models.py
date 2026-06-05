from django.utils import timezone

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Helper classes
class Unit(models.TextChoices):
    ML = "ml", "ml"
    G = "g", "g"
    PCS = "pcs", "Pieces"


# unique key? validators?
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = PhoneNumberField(unique=True)
    base_phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return " ".join(filter(None, [self.first_name, self.last_name]))

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "last_name"], name="unique_customer_name"
            )
        ]


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Sampoo, Conditioner etc
class ProductType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    size = models.PositiveIntegerField(blank=True, null=True)
    unit = models.CharField(
        max_length=10, choices=Unit.choices, default=Unit.ML, blank=True, null=True
    )
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    selling_price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        size_str = f"{self.size}{self.unit}" if self.size else ""
        return " ".join(filter(None, [str(self.brand), str(self.type), size_str]))


class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    date = models.DateTimeField(default=timezone.now)
    # TODO: should it support more than one user?
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    services = models.ManyToManyField(Service)
    duration = models.PositiveIntegerField(default=30)

    def save(self, *args, **kwargs):
        if self.duration is None:
            self.duration = self.date.hour + 30
        super().save(*args, **kwargs)

    def __str__(self):
         return f"{str(self.customer)} {str(self.date.month) +  "/" + str(self.date.month)}"

class AppointmentReport(models.Model):
    appointment = models.OneToOneField(
        Appointment, on_delete=models.CASCADE, related_name="report"
    )
    notes = models.TextField(blank=True, null=True)
    duration = models.PositiveIntegerField(default=30)
    # services? I want for him to able to simply choose but aslo to customize
