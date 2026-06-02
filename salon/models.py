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


class ProductType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, verbose_name="which brand is this"
    )
    type = models.ForeignKey(
        ProductType, on_delete=models.PROTECT, verbose_name="what product is this"
    )
    size = models.PositiveIntegerField(blank=True, null=True)
    unit = models.CharField(max_length=10, choices=Unit.choices, default=Unit.ML, blank=True, null=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    selling_price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        size_str = f"{self.size}{self.unit}" if self.size else ""
        return " ".join(filter(None, [str(self.brand), str(self.type), size_str]))
