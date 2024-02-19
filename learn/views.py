from django.shortcuts import render
# Create your views here.
from .models import Register
from django.core.cache import cache


def get_cached_register_data():
    cached_data = cache.get('cached_register_data')

    if cached_data is not None:
        print("Fetching data from cache")
        return cached_data

    data = list(Register.objects.all())

    cache.set('cached_register_data', data, timeout=60)

    return data


def index(request):
    data = get_cached_register_data()

    return render(request, 'index.html', {'data': data})
