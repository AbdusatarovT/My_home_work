from django.contrib import admin
from product.models import Category,Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'created_at']
    list_filter = ['category']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

