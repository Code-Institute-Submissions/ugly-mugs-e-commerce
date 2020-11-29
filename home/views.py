from django.shortcuts import render
from mugs.models import Mug
from mugs.views import mug_detail


def index(request):
    """ A view to return the index page """

    mugs = Mug.objects.all()

    context = {
        'mugs': mugs,
    }

    return render(request, 'home/index.html', context)


def about(request):
    """ A view to return the about page """

    mugs = Mug.objects.all()

    context = {
        'mugs': mugs,
    }

    return render(request, 'home/about.html', context)


def contact(request):
    """ A view to return the contact page """

    return render(request, 'home/contact.html')
