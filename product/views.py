from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView
from .models import Product

    
def productView(request):
    products = Product.objects.all()[:5]
    return render(request, 'product/product.html', {'products': products})