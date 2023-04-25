from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Games
from .forms import GamesForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Games.objects.all()
    query = None
    sort = None
    direction = None

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)