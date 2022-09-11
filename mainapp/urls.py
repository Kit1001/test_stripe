from django.urls import path

from mainapp import views

urlpatterns = [
    path('', views.index),
    path('buy_order', views.buy_order),
    path('item/<int:pk>', views.item, name='item'),
    path('buy/<int:pk>', views.buy),
    path('success', views.success),
    path('success_order/<int:pk>', views.success_order),
]
