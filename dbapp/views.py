from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def post(request):
    return render(request, 'post.html')