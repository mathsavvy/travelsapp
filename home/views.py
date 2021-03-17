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

# def signin(request):
#     return render(request, 'home/Login.html', {})
#
# def signup(request):
#     return render(request, 'home/Signup.html', {})
#
# def forgpass(request):
#     return render(request, 'home/Forgotpassword.html', {})

def about(request):
    return render(request, 'home/About.html', {})

def aboutus(request):
    return render(request,'home/AboutUs.html', {})

def contact(request):
    return render(request, 'home/Contact.html', {})

def contactus(request):
    return render(request,'home/Contactus.html',{})

# def auth(request):
#     try:
#         user = User.objects.get(username=request.POST['username'])
#         user_auth = authenticate(username=request.POST['username'], password=request.POST['password'])
#         print(user, request.POST['password'], user)
#         if user_auth is not None:
#             login(request, user_auth)
#             return HttpResponseRedirect(reverse('home'))
#     except (KeyError, User.DoesNotExist):
#         user_auth = None
#     if user_auth is None:
#         return render(request, "home/Login.html", {
#             "error_message": "Invalid email or password"
#         })
    
# def register(request):
#     m = request.POST['firstname'].lower()
#     x = m.isalpha()
#     n = request.POST['lastname'].lower()
#     y = n.isalpha()
#     z = request.POST['username'].isalnum()
#     a = str(request.POST['mobno'])
#     if len(request.POST['firstname'])<3:
#         return render(request, "home/Signup.html", {
#             "error_message": "*Enter a First name"
#         })
#     elif x!=1:
#         return render(request, "home/Signup.html", {
#             "error_message": "*Invalid First name"
#         })
#     elif y!=1:
#         return render(request, "home/Signup.html", {
#             "error_message": "*Invalid Last name"
#         })
#     elif len(request.POST['lastname'])<1:
#         return render(request, "home/Signup.html", {
#             "error_message": "*Enter a Last name"
#         })
#     elif len(request.POST['username'])<6:
#         return render(request, "home/Signup.html", {
#             "error_message": "*Username should have atleast 6 characters"
#         })
#     elif z!=1:
#         return render(request, "home/Signup.html", {
#             "error_message": "*Username should be alphanumeric"
#         })
#     elif User.objects.filter(username=request.POST['username']).exists():
#         return render(request, "home/Signup.html", {
#             "error_message": "*Username already exists"
#         })
#     elif len(request.POST['email'])<7:
#         return render(request, "home/Signup.html", {
#             "error_message": "*Invalid Email"
#         })
#     elif len(request.POST['regno'])!=9:
#         return render(request, "home/Signup.html", {
#             "error_message": "*Invalid registration number"
#         })
#     elif Extra.objects.filter(reg_no=request.POST['regno']).exists():
#         return render(request, "home/Signup.html", {
#             "error_message": "*Registration number already exists"
#         })
#     elif len(a)!=10:
#         return render(request, "home/Signup.html", {
#             "error_message": "*Invalid Mobile number"
#         })
#     elif len(request.POST['pass'])<6:
#         return render(request, "home/Signup.html", {
#             "error_message": "*Password should have more than 4 characters"
#         })
#     elif request.POST['pass']!=request.POST['repass']:
#         return render(request, "home/Signup.html", {
#             "error_message": "*Passwords dont match"
#         })
#     else:
#         newUser = User.objects.create_user(first_name=request.POST['firstname'], last_name=request.POST['lastname'], username=request.POST['username'], email=request.POST['email'],password=request.POST['pass'])
#         newExtra = Extra(reg_no=request.POST['regno'],mob_no=request.POST['mobno'])
#         newExtra.user = newUser
#         newExtra.save()
#         return HttpResponseRedirect(reverse('befsignin'))

# def retrieve(request):
#     try:
#         user = User.objects.get(email=request.POST['email'],username=request.POST['username'])
#         retre = authenticate(username=request.POST['username'])
#         print(user, request.POST['email'], user)
#         if retre is not None:
#             login(request, retre)
#             return HttpResponseRedirect(reverse('home'))
#     except (KeyError, Extra.DoesNotExist):
#         retre = None
#     if retre is None:
#         return render(request, "home/Forgotpassword.html", {
#             "error_message": "*Either E-mail or username does not exist"
#         })

def home(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('befsignin'))
        
    return HttpResponseRedirect(reverse('cab'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('befsignin'))
    
def cab(request):
    return render(request, "home/Cabspage.html", {})

def cab_book(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('befsignin'))

    newBook = CabRide(pickup=request.POST['pickup'],drop=request.POST['drop'],jourtype=request.POST['journeyType'])
    name = request.POST['name']
    contact = request.POST['contact']
    # newBook.user = request.user
    # newExtra = request.user.extra
    # newBook.save()
    # extradet = request.user.mob_no
    curname =str(name)
    contact = str(contact)
    return render(request ,"home/Confirmation.html", {
        'curname' : curname,
        'extradet' : contact,
        'pickplace' : newBook.pickup,
        'dropplace' : newBook.drop,
        'jourtype' : newBook.jourtype,
        'timebook' :newBook.time,
    })