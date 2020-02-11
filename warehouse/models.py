from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db import IntegrityError, transaction
from django.db.models import F

# Create your models here.

class Suppliers(models.Model):
    supplierID=models.CharField(max_length=250)
    companyName = models.CharField(max_length=255)
    slug=models.SlugField(max_length=250,unique=True)
    contactName = models.CharField(max_length=255)
    contactTitle = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.IntegerField()
    fax = models.CharField(max_length=255)
    homePage = models.CharField(max_length=255)
    class Meta:
        verbose_name='supplier'
        verbose_name_plural='supppliers'
    def get_absolute_url(self):
        return reverse('warehouse:list_of_suppliers',args=[self.slug])

    def __str__(self):
        return self.companyName

    def save(self, *args, **kwargs):
        self.slug = slugify(self.companyName)
        super(Suppliers, self).save(*args, **kwargs)

class Categories(models.Model):
    slug=models.SlugField(max_length=250,unique=True)
    categoryID=models.CharField(max_length=250)
    categoryName = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.ImageField(upload_to='static/images')



    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def get_absolute_url(self):
        return reverse('warehouse:list_of_products_by_category',kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.categoryName)
        super(Categories, self).save(*args, **kwargs)

        def image_tag(self):
            from django.utils.html import escape
            return u'<img src="%s" />' % escape()
            image_tag.short_description = 'Image'
            image_tag.allow_tags = True



    def __str__(self):
        return self.categoryName

class Products(models.Model):
    INSCTOCK = (
        ('instock', 'In_stock'),
        ('outofstock', 'Out_of_stock'),
    )
    ONORDER=(
        ('onorder','Onorder'),
        ('notonorder','None'),
    )
    DISCONTINUED=(
        ('discontinued','Discontinued'),
        ('continued', 'Continued'),
    )
    productID = models.CharField(max_length=255,unique=True)
    productName = models.CharField(max_length=255)
    slug=models.SlugField(max_length=250,unique=True)
    supplierID = models.ForeignKey(Suppliers,on_delete=models.CASCADE)
    categoryID = models.ForeignKey(Categories,on_delete=models.CASCADE)
    quantityPerUnit = models.IntegerField()
    unitPrice = models.IntegerField()
    unitsOnOrder = models.CharField(max_length=255,choices=ONORDER,default='None')
    reorderLevel = models.IntegerField()
    discontinued = models.CharField(max_length=255,choices=DISCONTINUED,default='Continued')
    author=models.ForeignKey(User,related_name='add_manager',on_delete=models.CASCADE)

    # quantity of ordered products

    def unitsInStock(self):
        if int(self.quantityPerUnit) > 0:
            self.unitsInStock = 'In_stock'
        else:
            self.unitsInStock = 'Out_of_stock'
        return self.unitsInStock


    class Meta:
        verbose_name='product'
        verbose_name_plural='products'

    def get_absolute_url(self):
        return reverse('warehouse:list_of_products',args=[self.slug])

    def __str__(self):
        return self.productName


    def save(self, *args, **kwargs):
        self.slug = slugify(self.productName)
        super(Products, self).save(*args, **kwargs)




class Order(models.Model):

    ORDER_STATUS=(
         ('draft','draft'),
        ('placed','Placed')
    )
    orderID=models.CharField(max_length=255)
    slug=models.SlugField(max_length=250,unique=True)
    productID = models.ForeignKey(Products,on_delete=models.CASCADE)
    unitPrice = models.IntegerField()
    quantity = models.IntegerField()
    discount = models.IntegerField()
    status=models.CharField(max_length=9,choices=ORDER_STATUS,default='Placed')
    orderDate=models.DateTimeField(default=timezone.now)

    def unitsOnOrder(self):
        self.unitsOnOder=0
        if int(self.quantity) > 0:
            self.unitsOnOder += int(self.quantity)

        return self.unitsOnOder


    def get_absolute_url(self):
        return reverse('warehouse:list_of_orders',args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.orderID)
        super(Order, self).save(*args, **kwargs)


    class Meta:
        verbose_name='order'
        verbose_name_plural='orders'






# Create your models here.

