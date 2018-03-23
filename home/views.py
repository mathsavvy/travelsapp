from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import CabRide
from django.utils import timezone


from .models import Extra

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'home/Index.html', {})

def signin(request):
    return render(request, 'home/Login.html', {})

def signup(request):
    return render(request, 'home/Signup.html', {})

def auth(request):
    try:
        user = User.objects.get(username=request.POST['username'])
        user_auth = authenticate(username=request.POST['username'], password=request.POST['password'])
        print(user, request.POST['password'], user)
        if user_auth is not None:
            login(request, user_auth)
            return HttpResponseRedirect(reverse('home'))
    except (KeyError, User.DoesNotExist):
        user_auth = None
    if user_auth is None:
        return render(request, "home/Login.html", {
            "error_message": "Invalid email or password"
        })
    
def register(request):
    newUser = User.objects.create_user(first_name=request.POST['firstname'], last_name=request.POST['lastname'], username=request.POST['username'], email=request.POST['email'],password=request.POST['pass'])
    
    newUser.save()
    newExtra = Extra(reg_no=request.POST['regno'],mob_no=request.POST['mobno'])
    newExtra.user = newUser
    newExtra.save()
    return HttpResponseRedirect(reverse('befsignin'))

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('befsignin'))
        
    return render(request ,"home/Home.html", {})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('befsignin'))
    
def cab(request):
    return render(request, "home/Cabspage.html", {})

def cab_book(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('befsignin'))

    newBook = CabRide(pickup=request.POST['pickup'],drop=request.POST['drop'],jourtype=request.POST['journeyType'])
    newBook.user = request.user
    newBook.save()
    # extradet = request.user.mob_no
    curname = newBook.user.first_name + " " + newBook.user.last_name
    dropplace = newBook.drop
    return render(request ,"home/Confirmation.html", {
        'curname' : curname,
        # 'extradet' : extradet,
        'pickplace' : newBook.pickup,
        'dropplace' : newBook.drop,
        'jourtype' : newBook.jourtype,
        'timebook' :newBook.time,
    })