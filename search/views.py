from importlib.resources import contents
from django.shortcuts import render
from django.db.models import Q 
from django.db import connection
from dbapp.models import Club, Facility, Scholarship, Post



def searchResult(request):
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        club = Club.objects.all().filter(
            Q(name__icontains=query) 
        )
        facility = Facility.objects.all().filter(
            Q(name__icontains=query) 
        )
        post = Post.objects.all().filter(
            Q(title__icontains=query)
        )
        scholarship = Scholarship.objects.all().filter(
            Q(name__icontains=query)
        )
        result = club.union(facility)
    
    return render(request, 'search.html', {'query':query, 'result':result, 'post':post, 'scholarship':scholarship})