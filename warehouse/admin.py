from django.contrib import admin
from .models import Order,Categories,Products,Suppliers
from django.db import IntegrityError, transaction
from django.db.models import F
# Register your models here.



# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('categoryName','categoryID','description','picture')
    search_fields = ('categoryName','categoryID')
    prepopulated_fields = {'slug':('categoryName',)}

admin.site.register(Categories,CategoryAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('orderID','productID','quantity','unitPrice',Order.unitsOnOrder)
    search_fields = ('orderID','productID')
    list_filter = ('status','quantity')
    prepopulated_fields = {'slug':('orderID',)}

admin.site.register(Order,OrderAdmin)




class ProductAdmin(admin.ModelAdmin):
    list_display = ('productID','productName','quantityPerUnit','unitPrice',Products.unitsInStock,'unitsOnOrder','supplierID')
    search_fields = ('productName','productID',)
    list_filter = ('supplierID','categoryID','productID','productName')
    prepopulated_fields = {'slug':('productName',)}

admin.site.register(Products,ProductAdmin)

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplierID','companyName','contactName','contactTitle','address','city','region','postalCode')
    search_fields = ('SupplierID', 'companyName')
    prepopulated_fields = {'slug': ('companyName',)}
admin.site.register(Suppliers,SupplierAdmin)