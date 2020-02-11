import pymongo
from django.shortcuts import render,get_object_or_404,redirect
from django.http import  HttpResponse
from .models import Order,Categories,Suppliers,Products
from django.db import IntegrityError, transaction






def index(request):
    products = Products.objects.all()
    suppliers = Suppliers.objects.all()
    categories = Categories.objects.all()
    template='warehouse/index.html'
    context={"products" : products, "suppliers" : suppliers, "categories" : categories}
    return render(request,template , context)


def list_of_orders(request):
    list_of_orders=Order.objects.all()
    template='warehouse/list_of_orders.html'
    context={'list_of_orders':list_of_orders}
    return render(request,template,context)

def order_detail(request, order_slug):
    order = get_object_or_404(Order, slug=order_slug)
    template = 'warehouse/order_detail.html'
    context = {'order': order}
    return render(request, template, context)


def list_of_categories(request):
    category_list=Categories.objects.all()
    template='warehouse/list_of_categories.html'
    context = {'category_list':category_list}
    return render(request, template, context)

def list_of_products(request):
    product_list=Products.objects.all()
    template='warehouse/list_of_products.html'
    context={'product_list': product_list}
    return render(request,template,context)


def list_of_suppliers(request):
    supplier_list=Suppliers.objects.all()
    template='warehouse/list_of_suppliers.html'
    context={'supplier_list': supplier_list}
    return render(request,template,context)





