from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('adjust/<item_id>/', views.adjust_cart, name='adjust_cart'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
