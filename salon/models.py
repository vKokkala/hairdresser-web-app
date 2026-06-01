from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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
        return f"{self.first_name} {self.last_name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "last_name"], name="unique_customer_name"
            )
        ]
