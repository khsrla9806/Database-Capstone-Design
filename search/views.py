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

def searchDetail(request, name):
    try:
        if Club.objects.get(name=name) is not None:
            result = Club.objects.get(name=name)
    except:
        pass
    
    try:
        if Facility.objects.get(name=name) is not None:
            result = Facility.objects.get(name=name)
    except:
        pass
    
    return render(request, 'search_detail.html', {'result' : result})