from django.shortcuts import render
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()  # отримуємо всі продукти
    return render(request, 'product_list.html', {'products': products})

# Create your views here.
