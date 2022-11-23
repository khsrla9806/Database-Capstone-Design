from django.contrib import auth
from django.contrib.auth import authenticate
from .models import User
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                student_id=request.POST['student_id'],)
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
        return render(request, 'login.html')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        password = request.POST['password']
        user = authenticate(request, student_id=student_id, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'student_id or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
