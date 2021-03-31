from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
from .models import User

# Create your views here.

def index(request):
    return render(request, 'login.html')

def logout(request):
    request.session.clear()
    return redirect('/')


def register(request):
    if request.method=='POST':
        errors = User.objects.validator(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/')
        else:
            user_password = request.POST['password']
            hash_password = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(
                first=request.POST['first'],
                last=request.POST['last'],
                email=request.POST['email'],
                password=hash_password,
            )
            request.session['user_id'] = new_user.id
            request.session['user_name'] = f"{new_user.first} {new_user.last}"
            return redirect('/success')
    else:
        return redirect('/')

def login(request):
    if request.method=='POST':
        known_user=User.objects.filter(email=request.POST['email'])
        if known_user:
            known_user = known_user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), known_user.password.encode()):
                request.session['user_id'] = known_user.id
                request.session['user_name'] = f"{known_user.first} {known_user.last}"
                return redirect('/success')
    else:
        return redirect('/')



def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, 'success.html')