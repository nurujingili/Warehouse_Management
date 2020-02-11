from django.test import SimpleTestCase
from unittest import TestCase
from django.test import TestCase
from django.urls import reverse,resolve
from warehouse.views import index,list_of_orders,list_of_products,list_of_categories,list_of_suppliers

class TestUrls(TestCase):
    def test_index_url_is_resolved(self):
        url=reverse('warehouse:index')
        print(resolve(url))
        self.assertEqual(resolve(url).func,index)

    def test_product_list_url_is_resolved(self):
        url=reverse('warehouse:list_of_products')
        print(resolve(url))
        self.assertEqual(resolve(url).func,list_of_products)

    def test_order_list_url_is_resolved(self):
        url=reverse('warehouse:list_of_orders')
        print(resolve(url))
        self.assertEqual(resolve(url).func,list_of_orders)


    def test_category_list_url_is_resolved(self):
        url=reverse('warehouse:list_of_categories')
        print(resolve(url))
        self.assertEqual(resolve(url).func,list_of_categories)


    def test_supplier_list_url_is_resolved(self):
        url=reverse('warehouse:list_of_suppliers')
        print(resolve(url))
        self.assertEqual(resolve(url).func,list_of_suppliers)

