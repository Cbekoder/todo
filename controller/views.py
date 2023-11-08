from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, wraps
from .models import *
def my_login_required(redirect_url=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect(redirect_url or reverse('login'))
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usernames = users.objects.all().values(login)
        if username in usernames:
            passwo = users.objects.get(login = username)
            if passwo == password:
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
                return redirect('home')
        else:
            # messages =  'Invalid username or password'
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

# @my_login_required(redirect_url='login/')
def home(request):
    return render(request, 'index.html')

def edit(request):
    return render(request, 'edit.html')

def signup(request):
    return render(request, 'signup.html')

# def login(request):
#     return render(request, 'login.html')

