from django.contrib import admin
from .models import Customer
from .models import Category
from .models import Products
from .models import Order
from .models import slider

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(slider)
