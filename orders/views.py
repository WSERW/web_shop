import json
from django.shortcuts import render, HttpResponse
from .models import OrderItem, CallRequest
from .forms import OrderCreateForm, RequestCreateForm
from cart.cart import Cart
# from .tasks import order_created

# Create your views here.


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                order_item = OrderItem(order=order,
                                       product=item['product'],
                                       price=item['price'],
                                       quantity=item['quantity'])
                order_item.save()
            cart.clear()
            # order_created.delay(order.id)
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})


def call_request_create(request):
    if request.method == 'POST':
        client_name = request.POST.get('name', False)
        client_phone = request.POST.get('phone', False)
        client_license = request.POST.get('license', False)
        if not client_license:
            response = json.dumps({
                'status': False,
                'text': 'Подтвердите политику безопасности'
            })
            return HttpResponse(response)
        if client_name and client_phone:
            call_request = CallRequest(
                name=client_name,
                phone=client_phone,
            )
            call_request.save()
            response = json.dumps({
                'status': True,
                'text': "Спасибо с вами свяжутся!"
            })
            return HttpResponse(response)
        else:
            response = json.dumps({
                'status': False,
                'text': "Укажите данные!"
            })
            return HttpResponse(response)
    return HttpResponse("Произошла ошибка")
