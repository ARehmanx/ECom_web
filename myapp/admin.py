from django.contrib import admin
from .models import Products, Categories, Brands, PdctImgs, Reviews, Cart, Address, Order_Items, Complete_Order

# Register your models here.

admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Brands)
admin.site.register(PdctImgs)
admin.site.register(Reviews)
admin.site.register(Cart)
admin.site.register(Order_Items)
admin.site.register(Address)
admin.site.register(Complete_Order)
