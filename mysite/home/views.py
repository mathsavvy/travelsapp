from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import User

def index(request):
    return render(request, 'home/Index.html', {})

def signin(request):
    return render(request, 'home/Login.html', {})

def signup(request):
    return render(request, 'home/Signup.html', {})

def auth(request):
    try:
        selected_user = User.objects.get(e_mail=request.POST['email'], passwd=request.POST['password'])
        request.session['user_logged_name'] = selected_user.name
        request.session['user_logged_id'] = selected_user.user_id
    except (KeyError, User.DoesNotExist):
        return render(request, 'home/Login.html', {
            'error_message': "*Invalid User name or Password",
        })
    else:
        return HttpResponseRedirect(reverse('home'))
    
def register(request):
    newUser = User(name=request.POST['name'], e_mail=request.POST['email'],reg_no=request.POST['regno'],mob_no=request.POST['mobno'],alt_mob=request.POST['altmob'], passwd=request.POST['pass'])
    newUser.save()
    return render(request, 'home/Home.html', {})

def home(request):
    user_logged_id = request.session['user_logged_id']
    user_logged = User.objects.get(pk=user_logged_id)
    session_user_name = request.session['user_logged_name']
    template = loader.get_template('home/Home.html')
    return HttpResponse(template.render({}, request))

def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return HttpResponseRedirect(reverse('index'))