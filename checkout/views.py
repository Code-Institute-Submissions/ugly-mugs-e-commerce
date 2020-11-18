from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from .forms import OrderForm


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'checkout/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified mug to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


#def adjust_cart(request, item_id):
#    """ Adjust the quantity of the specified mug to the specified amount """
#
#    quantity = int(request.POST.get('quantity'))
#
 #   cart = request.session.get('cart', {})
#
#    if quantity > 0:
##        cart[item_id] = quantity
#    else:
 #       cart.pop(item_id)
#
 #   request.session['cart'] = cart
#    return redirect(reverse('view_cart'))


#def remove_from_cart(request, item_id):
#    """ Adjust the quantity of the specified mug to the specified amount """
#
 #   try:
#        cart = request.session.get('cart', {})
#        cart.pop(item_id)
#
#        request.session['cart'] = cart
#        return HttpResponse(status=200)
#
 #   except Exception as e:
#        return HttpResponse(status=500)


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('mugs'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HjVihGzTE5Kpg61pU4Wy2EsmF5jMXfHCaAMkQRaYaxXK0dR6xYGLncOOSYEtbrJduvaesrgUH6zNW6qKoE0y7QY00p16sRT7Y',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)