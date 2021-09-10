from django.db import models


class Brands(models.Model):
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.brand


class Categories(models.Model):
    category = models.CharField(max_length=100)
    brands = models.ForeignKey(Brands, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.category


class Products(models.Model):
    brands = models.ForeignKey(Brands, on_delete=models.CASCADE, null=True, related_name='brands')
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, related_name='categories')
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    img = models.ImageField()
    discount = models.BooleanField(default=False)
    discounted_price = models.IntegerField(default=0)
    is_promotion = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PdctImgs(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    imgs = models.ImageField(upload_to='product/images')

    def __str__(self):
        return self.product


class Reviews(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    review = models.TextField(max_length=255)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name


class Address(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    phone_num = models.IntegerField(default=0)
    street_address = models.TextField()
    zip_code = models.IntegerField(default=0)

    def __str__(self):
        return self.f_name


class Order_Items(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Complete_Order(models.Model):
    order = models.ForeignKey(Order_Items, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.order.name)