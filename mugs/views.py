from django.shortcuts import render
from .models import Mugs


def mugs(request):
    """ A view to show the collection page, including sorting and filtering """

    mugs = Mugs.objects.all()

    context = {
        'mugs': mugs,
    }

    return render(request, 'mugs/mugs.html', context)
