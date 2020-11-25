from django.shortcuts import render, get_object_or_404
from .models import Mug


def mugs(request):
    """ A view to show the collection page, including sorting and filtering """

    mugs = Mug.objects.all()

    context = {
        'mugs': mugs,
    }

    return render(request, 'mugs/mugs.html', context)


def mug_detail(request, mug_id):
    """ A view to show individual mug details """

    mug = get_object_or_404(Mug, pk=mug_id)

    context = {
        'mug': mug,
    }

    return render(request, 'mugs/mug_detail.html', context)
