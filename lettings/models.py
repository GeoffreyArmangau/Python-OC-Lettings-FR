"""Database models for the lettings app: postal addresses and rental listings."""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """A postal address, owned by exactly one Letting.

    number: house/building number (max 4 digits).
    street: street name.
    city: city name.
    state: 2-letter state code (e.g. US state abbreviation).
    zip_code: postal code (max 5 digits).
    country_iso_code: 3-letter ISO country code.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """Model metadata: fixes the "Addresses" plural (Django would default to "Addresss")."""

        verbose_name_plural = 'Addresses'

    def __str__(self):
        """Return "<number> <street>", e.g. "12 Main Street"."""
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """A rental listing: a title paired with a single Address.

    title: display name of the listing.
    address: the Address for this listing (one Letting per Address).
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Return the listing's title."""
        return self.title
