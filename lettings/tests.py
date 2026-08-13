"""Tests for the lettings app: models, URLs and views."""
from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


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


class LettingsUrlTests(TestCase):
    """Tests for the lettings app URL configuration."""

    def test_index_url_resolves(self):
        """The lettings:index route maps to /lettings/."""
        self.assertEqual(reverse('lettings:index'), '/lettings/')

    def test_letting_url_resolves(self):
        """The lettings:letting route maps to /lettings/<id>/."""
        self.assertEqual(reverse('lettings:letting', args=[1]), '/lettings/1/')


class LettingsViewTests(TestCase):
    """Tests for the lettings app views."""

    def setUp(self):
        """Create a letting available to every test in this class."""
        self.letting = create_letting(title='Cozy Cabin')

    def test_index_view_status_code_and_template(self):
        """The index view returns 200, uses the right template and lists the letting."""
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertIn(self.letting, response.context['lettings_list'])

    def test_letting_view_status_code_and_context(self):
        """The letting view returns 200, uses the right template and context."""
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertEqual(response.context['title'], 'Cozy Cabin')
        self.assertEqual(response.context['address'], self.letting.address)

    def test_letting_view_missing_letting_raises(self):
        """An unknown letting_id raises Letting.DoesNotExist (unhandled -> 500 in production)."""
        with self.assertRaises(Letting.DoesNotExist):
            self.client.get(reverse('lettings:letting', args=[9999]))
