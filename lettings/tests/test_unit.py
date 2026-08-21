"""Unit tests for the lettings app: model behavior in isolation."""
from django.test import TestCase

from ..models import Address, Letting


def create_address():
    """Create and return an Address for use in tests."""
    return Address.objects.create(
        number=12,
        street='Main Street',
        city='Springfield',
        state='IL',
        zip_code=62701,
        country_iso_code='USA',
    )


def create_letting(title):
    """Create and return a Letting (with its own Address) for use in tests."""
    return Letting.objects.create(title=title, address=create_address())


class AddressModelTests(TestCase):
    """Tests for the Address model."""

    def test_str_returns_number_and_street(self):
        """__str__ returns "<number> <street>"."""
        address = create_address()
        self.assertEqual(str(address), '12 Main Street')

    def test_verbose_name_plural_is_addresses(self):
        """The admin plural label is fixed to "Addresses" (not the default "Addresss")."""
        self.assertEqual(Address._meta.verbose_name_plural, 'Addresses')


class LettingModelTests(TestCase):
    """Tests for the Letting model."""

    def test_str_returns_title(self):
        """__str__ returns the letting's title."""
        letting = create_letting(title='Cozy Cabin')
        self.assertEqual(str(letting), 'Cozy Cabin')
