from django.test import TestCase, Client
from shop.models import Product, Purchase
from shop.views import PurchaseCreate


class PurchaseCreateTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(name="book", price=740, rest=5)

    def test_webpage_accessibility(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_page_displays_products(self):
        response = self.client.get('/')
        self.assertContains(response, self.product.name)
        self.assertContains(response, self.product.price)
