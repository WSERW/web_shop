from django.shortcuts import render, get_object_or_404
from django.db.models import Q,CharField
from django.db.models.functions import Lower
from .models import Category, Product, ProductImage
from promo.models import PromoBaner, PromoSlider
from cart.forms import CartAddProductForm

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    baner = PromoBaner.objects.all()[0]
    slider = PromoSlider.objects.all()[0]

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(Q(category=category) | Q(category__parent=category))
    else:
        products = products[:12]
    return render(request, 'shop/product/list.html', {'category':category,
                                                    'categories':categories,
                                                    'products':products,
                                                    'baner':baner,
                                                    'slider':slider,
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
    query = request.GET.get('q')
    categories = Category.objects.all()
    products = Product.objects.filter(Q(name__icontains=query) | Q(category__name__icontains=query))
    return render(request, 'shop/product/search.html', {'category':category,
                                                    'categories':categories,
                                                    'products':products})

def pay(request):
    return render (request, 'shop/pay.html',{})

def garant(request):
    return render (request, 'shop/garant.html',{})

def delivery(request):
    return render (request, 'shop/delivery.html',{})