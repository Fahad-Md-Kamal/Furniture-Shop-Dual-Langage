from django.shortcuts import render, HttpResponse
from django.utils.translation import gettext as _

from . import models


def home(request):
    context = {    }
    return render(request, 'product_app/home.html', context)


def product_list(request):
    context = {
        'products': models.Product.objects.all(),
        'categories': models.PRODUCT_CATEGORY
    }
    return render(request, 'product_app/product_list.html', context)
