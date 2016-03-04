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

    '''
    # The following are useful for returning links versus string representations
    reviews = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='review-detail'
    )
    '''

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



class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('path', 'product')


