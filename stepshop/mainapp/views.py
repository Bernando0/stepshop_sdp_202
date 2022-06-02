from django.shortcuts import render
from mainapp.models import Product, ProductCategory

links_menu = [
    {'href': 'index', 'name': 'Домой', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
]

def products(request):
    title = 'Продукты'

    products_ = Product.objects.all()
    categories_ = ProductCategory.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products_,
        'categories': categories_,
    }

    return render(request, "products.html", context)


def product(request):
    return render(request, "product.html")
# Create your views here.
