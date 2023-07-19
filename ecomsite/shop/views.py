from django.shortcuts import render
from .models import *

# Create your views here.



def home(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    context = {
        'products':products,
        'categories':categories,
    }
    return render(request, 'shop/index.html', context=context)
