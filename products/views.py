from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Product
from django.views.generic import ListView
import json


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {
        'products': products
    })


def new(request):
    return HttpResponse("This is the New section!")


def json_response(request):
    data = list(Product.objects.values())
    return JsonResponse(data, safe=False)
