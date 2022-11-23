from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signin(request):
    return render(request, 'signin.html')

def post(request):
    return render(request, 'post.html')