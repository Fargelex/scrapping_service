from django.shortcuts import render

from .forms import FindForm
from .models import Vacancy


# Create your views here.


def home_view(request):
    city = request.GET.get('city')
    language = request.GET.get('language')
    form = FindForm()
    qs = []
    _filter = {}
    if city or language:
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language

    qs = Vacancy.objects.filter(**_filter)
    return render(request, 'scraping/home.html', {'object_list': qs, 'form': form})
