import stripe
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

from mainapp.models import Item

stripe.api_key = 'sk_test_51LfpHZJtMpkSmDUETSDRZdMCDL3yGHPpAydEUJOCOw7yyJB414jnVthsHOOtzn4jNinyy735kNdMIXDenNHQ556G00y7WRiOGo'


def item(request, pk):
    product = get_object_or_404(Item, pk=pk)
    # print('do we get here')
    # return HttpResponse(f'{product.id} - <img src={settings.MEDIA_URL}{product.image}></img>')

    return render(request, 'mainapp/item.html', {"product": product})


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
        success_url='https://google.com',
        cancel_url='https://yandex.ru',

    )

    return JsonResponse(session)


def test(request):
    print(request.build_absolute_uri('/'))
    return HttpResponse()


def test_response(request):
    return JsonResponse({'foo': {'zap': 'bar'}})
