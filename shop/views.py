from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, Product, ProductImage
from cart.forms import CartAddProductForm

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(Q(category=category) | Q(category__parent=category))
    return render(request, 'shop/product/list.html', {'category':category,
                                                    'categories':categories,
                                                    'products':products,
                                                    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form':cart_product_form})

def product_search(request):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(name__contains=request.GET.get('q'))
    return render(request, 'shop/product/search.html', {'category':category,
                                                    'categories':categories,
                                                    'products':products})

def pay(request):
    return render (request, 'shop/pay.html',{})

def garant(request):
    return render (request, 'shop/garant.html',{})

def delivery(request):
    return render (request, 'shop/delivery.html',{})