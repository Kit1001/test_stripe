from django.urls import path

from mainapp import views

urlpatterns = [
    path('exp', views.test),
    path('api', views.test_response),
    path('test', views.test_response, name='test'),
    path('item/<int:pk>', views.item),
    path('buy/<int:pk>', views.buy)
]
