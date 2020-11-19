from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from mugs.models import Mug
from checkout.contexts import cart_contents

import stripe


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'checkout/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified mug to the shopping cart """

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
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY


    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                try:
                    mug = Mug.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        mug=mug,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Mug.DoesNotExist:
                    messages.error(request, (
                        "One of the mugs in your cart wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request,
                           "There's nothing in your cart at the moment")
            return redirect(reverse('mugs'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
