from django.shortcuts import render

from mainapp.models import Product, Category

# Create your views here.
def index(request):
    context = {
        'products' : Product.objects.all()[:4]
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'links_menu': Category.objects.all()
    }

    return render(request, 'mainapp/products.html', context)


def products_list(request, pk):
    print(pk)
    context = {
        'links_menu': Category.objects.all()
    }
    return render(request, 'mainapp/products.html')



def contact(request):
    return render(request, 'mainapp/contact.html')
"""
select count(1) from mainapp_products where price >= 100;
"""
