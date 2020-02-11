import unittest
from unittest import TestCase
from django.urls import reverse
from warehouse.models import Order,Categories,Suppliers,Products


class TestModels(unittest.TestCase):
    def setUp(self):
        self.quantity = 10
        self.quantityPerUnit = 20

    def test_Units_On_Stock(self):
        self.product1 = Products.objects.create(
            productID='product1',
            productName='Sheets',
            quantityPerUnit=10,
            unitPrice=12,
            unitsOnOrder='None',
            reorderLevel=0,
            discontinued='Continued'

        )
        self.assertEquals(self.product1.unitsInStock(),'In_stock')


    def test_Units_On_Order(self):
        self.order1 = Order.objects.create(
            orderID='order1',
            quantity=10,
            unitPrice=7,
            discount=0
        )
        self.assertEquals(self.order1.unitsOnOrder(),10)








