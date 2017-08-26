from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from store.models import Product

class IndexView(generic.ListView):
    template_name = 'index.html'
    # The following context object will be available to django templates with the actual context set by
    # the get_queryset method (djb - 26 Aug 17)
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()