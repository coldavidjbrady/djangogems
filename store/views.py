from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets, authentication, permissions, filters
from .models import *
from .serializers import *
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.

class DefaultMixin(object):
    authentication_classes = (
        #authentication.CSRFCheck
        authentication.BasicAuthentication,
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
        JSONWebTokenAuthentication
    )
    permission_classes = (
        permissions.IsAuthenticated,
        #permissions.IsAuthenticatedOrReadOnly,
        #permissions.AllowAny,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

class ProductViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ImageViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ReviewViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer