from unittest import TestCase
from django.test import TestCase,Client
from django.urls import reverse
from mixer.backend.django import mixer
from warehouse.views import index,list_of_orders,list_of_products,list_of_categories,list_of_suppliers

class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
        self.index_url=reverse('warehouse:index')
        self.list_url=reverse('warehouse:list_of_orders')
        self.product_list_url = reverse('warehouse:list_of_products')
        self.category_list_url = reverse('warehouse:list_of_categories')
        self.supplier_list_url = reverse('warehouse:list_of_suppliers')

    def test_index_page(self):
        response=self.client.get(self.index_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'warehouse/index.html')

    def test_list_of_orders(self):
        response=self.client.get(self.list_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'warehouse/list_of_orders.html')

    def test_list_of_products(self):
        response = self.client.get(self.product_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'warehouse/list_of_products.html')

    def test_list_of_categories(self):
        response = self.client.get(self.category_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'warehouse/list_of_categories.html')

    def test_list_of_suppliers(self):
        response = self.client.get(self.supplier_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'warehouse/list_of_suppliers.html')




