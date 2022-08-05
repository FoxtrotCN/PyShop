from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Product
from django.views.generic import ListView
import json


def home(request):
    products = Product.objects.all()
    return render(request, 'pyshop/home.html', {
        'products': products
    })


def cart(request):
    return render(request, 'pyshop/cart.html')



















# def json_response(request):
#     data = list(Product.objects.values())
#     return JsonResponse(data, safe=False)
