#from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import *

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('path', )


class ReviewSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('stars', 'body', 'author', 'createdOn', 'product', 'links')

    def get_links(self, obj):
        request = self.context['request']
        links = {
            'self': reverse('review-detail', kwargs={'pk':obj.pk}, request=request),

        }
        return links


class ProductSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    reviews = ReviewSerializer(many=True, read_only=True)
    images = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='path'
     )

    class Meta:
      model = Product
      fields = ('id', 'name','shine', 'price', 'rarity', 'color',
                  'faces', 'links','reviews', 'images')

    def get_links(self, obj):
        request = self.context['request']
        links = {
            'self': reverse('product-detail', kwargs={'pk':obj.pk}, request=request),

        }
        return links








