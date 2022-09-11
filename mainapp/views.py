import json

import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from mainapp.models import Item, Order

stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    products = Item.objects.all()

    products_json = dict()
    for product in products:
        products_json[product.id] = {
            'name': product.name,
            'price': product.price
        }

    products_json = json.dumps(products_json)

    return render(request, 'mainapp/index.html', {"products": products,
                                                  "products_json": products_json,
                                                  "stripe_key": settings.STRIPE_PUBLIC_KEY},
                  )


def item(request, pk):
    product = get_object_or_404(Item, pk=pk)

    return render(request, 'mainapp/item.html', {"product": product, "stripe_key": settings.STRIPE_PUBLIC_KEY})


def buy(request, pk):
    product = get_object_or_404(Item, pk=pk)
    product_data = {
        "name": product.name,
        "description": product.description,
        'images': [f'{request.build_absolute_uri("/")}{product.image.url}'],
    }

    price_data = {
        "currency": 'RUB',
        'unit_amount': product.price * 100,
        "product_data": product_data,
    }

    session = stripe.checkout.Session.create(
        line_items=[
            {"quantity": 1,
             "price_data": price_data,
             },
        ],
        mode='payment',
        success_url=f'{request.build_absolute_uri("/success")}',
        cancel_url=f'{request.build_absolute_uri(f"/item/{product.id}")}',

    )
    return JsonResponse(session)


def buy_order(request):
    products = json.loads(request.body)
    line_items = []
    for p_id in products:
        quantity = products[p_id].get('quantity')
        if quantity:
            product = Item.objects.get(pk=p_id)
            line_item = {"quantity": quantity,
                         "price_data": {
                             "currency": 'RUB',
                             'unit_amount': product.price * 100,
                             "product_data": {
                                 "name": product.name,
                                 "description": product.description,
                                 'images': [f'{request.build_absolute_uri("/")}{product.image.url}'],
                             },
                         },
                         }
            line_items.append(line_item)

    order = Order(details=products, status='P')
    order.save()

    session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        success_url=f'{request.build_absolute_uri(f"/success_order/{order.id}")}',
        cancel_url=f'{request.build_absolute_uri("/")}',
    )

    return JsonResponse(session)


def success(request):
    return HttpResponse('Payment successful')


def success_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.status = 'S'
    order.save()
    response = redirect('/')
    return response
