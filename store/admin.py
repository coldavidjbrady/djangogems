from django.contrib import admin
from .models import Product, Review, Image

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description', 'shine', 'rarity', 'price', 'color', 'faces']}),
    ]

class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['stars', 'body', 'shine', 'author', 'price', 'createdOn', 'product']}),
    ]

class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['path', 'product']}),
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Image, ImageAdmin)
