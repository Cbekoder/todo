from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from .models import *

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST.get('l'),
            password = request.POST.get('p')
        )
        if user is None:
            return redirect("/login/")
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'login.html')

def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get("name") != None and request.POST.get("date") != None:
                Tasks.objects.create(
                    title = request.POST.get("name"),
                    date = request.POST.get("date"),
                    text = request.POST.get("details"),
                    condition = request.POST.get("status"),
                    userid = request.user,
                )
            return redirect('/')
        content = {
            'tasks' : Tasks.objects.filter(userid = request.user),
            'username' : request.user.username.capitalize()
        }
        return render(request, 'index.html', content)
    return redirect("/login")

def edit(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            ts = Tasks.objects.get(id=id)
            ts.title = request.POST.get('name')
            ts.text = request.POST.get('detail')
            ts.condition = request.POST.get('status')
            ts.save()
            return redirect('/')
        content = {
            'task' : Tasks.objects.get(id = id),
            'username' : request.user.username.capitalize()
        }
        return render(request, 'edit.html', content)
    return redirect("/login")

def delete(request, id):
    if request.user.is_authenticated:
        ts = Tasks.objects.get(id=id)
        if ts.userid == request.user:
            ts.delete()
            return redirect('/')
    return redirect('/')

def signup(request):
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('/')

