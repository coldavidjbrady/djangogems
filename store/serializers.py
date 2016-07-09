#from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import *

class ReviewSerializer(serializers.ModelSerializer):

    revlinks = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('stars', 'body', 'author', 'createdOn', 'product', 'revlinks')

    def get_revlinks(self, obj):
        request = self.context['request']
        revlinks = {
            'self': reverse('review-detail', kwargs={'pk':obj.pk}, request=request),
        }
        return revlinks

    def __str__(self):
        return '%d: %s' % self.id, self.product.name

class ProductSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True)
    images = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='path'
     )

    class Meta:
      model = Product
      fields = ('id', 'name', 'description', 'shine', 'price', 'rarity', 'color',
                  'faces', 'links', 'reviews', 'images')


    def get_links(self, obj):
        request = self.context['request']
        links = {
            'self': reverse('product-detail', kwargs={'pk':obj.pk}, request=request),
        }
        return links

    def update(self, instance, update_data):
        # Update the product instance
        instance.name = update_data['name']
        instance.description = update_data['description']
        instance.shine = update_data['shine']
        instance.price = update_data['price']
        instance.rarity = update_data['rarity']
        instance.color = update_data['color']
        instance.faces = update_data['faces']
        instance.save()
        return instance

    def create(self, data):
        # Create the product instance
        newProduct = Product.objects.create(name=data["name"], description=data["description"], shine=data["shine"],
                                            price=data["price"], rarity=data["rarity"], color=data["color"], faces=data["faces"])
        newProduct.save()
        return newProduct

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('path', 'product')


