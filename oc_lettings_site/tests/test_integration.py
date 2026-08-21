"""Integration tests for the oc_lettings_site app: home page, root URL and custom error pages."""
from django.test import Client, TestCase
from django.test.utils import override_settings
from django.urls import reverse


class HomeViewTests(TestCase):
    """Tests for the home page view."""

    def test_index_view_status_code_and_template(self):
        """The home page returns 200 and renders index.html."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class IndexUrlTests(TestCase):
    """Tests for the root URL configuration."""

    def test_index_url_resolves(self):
        """The index route maps to /."""
        self.assertEqual(reverse('index'), '/')


class ErrorPageTests(TestCase):
    """Tests for the custom 404/500 pages, only rendered by Django when DEBUG=False."""

    @override_settings(DEBUG=False, ALLOWED_HOSTS=['testserver'])
    def test_404_page_uses_custom_template(self):
        """An unknown URL returns 404 and renders the custom 404.html template."""
        response = self.client.get('/this-url-does-not-exist/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    @override_settings(DEBUG=False, ALLOWED_HOSTS=['testserver'])
    def test_500_page_uses_custom_template(self):
        """An unhandled server error returns 500 and renders the custom 500.html template."""
        client = Client(raise_request_exception=False)
        response = client.get('/lettings/99999/')
        self.assertEqual(response.status_code, 500)
        self.assertTemplateUsed(response, '500.html')
