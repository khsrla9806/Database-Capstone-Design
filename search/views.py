from importlib.resources import contents
from django.shortcuts import render
from django.db.models import Q 
from dbapp.models import Club;



def searchResult(request):
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        clubs = Club.objects.all().filter(
            Q(name__icontains=query) |
            Q(image__icontains=query) |
            Q(content__icontains=query)
        )
    return render(request, 'search.html', {'query':query, 'clubs':clubs})
