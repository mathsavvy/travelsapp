from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import User

def index(request):
    if(request.session.get('user_logged_id')):
        return render(request, 'Website/home.html')
    else:
        return render(request, 'Website/Home.html')

def auth(request):
    try:
        selected_user = User.objects.get(name=request.POST['mobile_number'],password=request.POST['password'])
        request.session['user_logged_name'] = selected_user.name
        request.session['user_logged_id'] = selected_user.user_id
    except(KeyError, User.DoesNotExist):
        return render(request,'Website/Login.html',{
            'error_message':"*Invalid Mobile number or password!",
            })
    else:
        return HttpResponseRedirect(reverse('home'))

def register(request):
    try:
        newUser = User(name=request.POST['name'],register_number=request.POST['register_name'],mobile_number=request.POST['mobile_number'],password=request.POST['password'])
    except(KeyError, User.is_valid()):
        newUser.save()
        return HttpResponseRedirect(index)
    else:
        return render(request,'Website/Signup.html',{
            'error_message':"*The mobile number or password that you entered already exists!",
        })

def home(request):
    user_logged_id = request.session['user_logged_id']
    user_logged = User.objects.get(pk=user_logged_id)
    template = loader.get_template('Website/home.html')
    return HttpResponse(template.render(request))

def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return HttpResponseRedirect(reverse('index')) 