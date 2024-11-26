from django.test import TestCase
from shop.models import Product, Purchase
from datetime import datetime


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="book", price="740", rest=10)
        Product.objects.create(name="pencil", price="50", rest=0)

    def test_correctness_types(self):
        self.assertIsInstance(Product.objects.get(name="book").name, str)
        self.assertIsInstance(Product.objects.get(name="book").price, int)
        self.assertIsInstance(Product.objects.get(name="book").rest, int)
        self.assertIsInstance(Product.objects.get(name="pencil").name, str)
        self.assertIsInstance(Product.objects.get(name="pencil").price, int)        

    def test_correctness_data(self):
        self.assertEqual(Product.objects.get(name="book").price, 740)
        self.assertEqual(Product.objects.get(name="pencil").price, 50)
        self.assertEqual(Product.objects.get(name="book").rest, 10)
        self.assertEqual(Product.objects.get(name="pencil").rest, 0)

    def test_product_rest_reduction(self):
        product = Product.objects.get(name="book")
        initial_rest = product.rest
        product.rest -= 1
        product.save()
        self.assertEqual(product.rest, initial_rest - 1)


class PurchaseTestCase(TestCase):
    def setUp(self):
        self.product_book = Product.objects.create(name="book", price="740", rest=10)
        self.datetime = datetime.now()
        Purchase.objects.create(product=self.product_book,
                                person="Ivanov",
                                address="Svetlaya St.")

    def test_correctness_types(self):
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).person, str)
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).address, str)
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).date, datetime)

    def test_correctness_data(self):
        self.assertTrue(Purchase.objects.get(product=self.product_book).person == "Ivanov")
        self.assertTrue(Purchase.objects.get(product=self.product_book).address == "Svetlaya St.")
        self.assertTrue(Purchase.objects.get(product=self.product_book).date.replace(microsecond=0) == \
            self.datetime.replace(microsecond=0))

    def test_product_stock_decreases_on_purchase(self):
        product = Product.objects.create(name="notebook", price=100, rest=5)
        Purchase.objects.create(product=product, person="Petrov", address="Lenina St.")
        product.rest -= 1
        product.save()
        # product.refresh_from_db()
        self.assertEqual(product.rest, 4)
