from django.contrib import admin

# Register your models here.
from .models import Product, Category, Discount, Cart


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(Cart)