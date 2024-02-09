from django.shortcuts import render

from food_app.models import ProductCategory, Product


# Create your views here.

def main_page(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all().order_by('-id')
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'templates/index.html', context=context)


def menu_page(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all().order_by('-id')
    burger = Product.objects.filter(category_id__name='BURGER').order_by('-id')
    pitsas = Product.objects.filter(category_id__name='PITSA').order_by('-id')
    kartoshka_fri = Product.objects.filter(category_id__name='KARTOSHKA FRI').order_by('-id')
    lavash = Product.objects.filter(category_id__name='LAVASH').order_by('-id')
    context = {
        'products': products,
        'categories': categories,
        'burger': burger,
        'pitsas': pitsas,
        'kartoshka_fri': kartoshka_fri,
        'lavash': lavash,
    }
    return render(request, 'templates/menu.html', context=context)


def about_page(request):
    return render(request, 'templates/about.html')


def book_page(request):
    return render(request, 'templates/book.html')
