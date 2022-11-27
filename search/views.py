from importlib.resources import contents
from django.shortcuts import render
from django.db.models import Q 
from django.db import connection
from dbapp.models import Club,Facility;



def searchResult(request):
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        club = Club.objects.all().filter(
            Q(name__icontains=query) 
        )
        facility = Facility.objects.all().filter(
            Q(name__icontains=query) 
        )
        result = club.union(facility)
        print(result)
    return render(request, 'search.html', {'query':query, 'result':result})