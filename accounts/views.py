from django.shortcuts import render
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from schedule.models import UserScore
from accounts.models import UserContact
# Create your views here.

def login_view (request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is None: 
            context = {"error": "invalid username"}
            return render(request,  'accounts/login.html', context )
        login(request,user)

        
        return redirect('/desk')
    return render(request,  'accounts/login.html', {})
    
def logout_view (request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    return render(request,  'accounts/logout.html', {})

def register_view (request):
    if request.method =="POST" :
        userName  = request.POST.get('username', None)
        userPass  = request.POST.get('password', None)
        userPass2 = request.POST.get('password2', None)
        instagram    = request.POST.get('instagram', None)


        # TODO: check if already existed
        if userName and userPass and (userPass==userPass2):
           u,created = User.objects.get_or_create(username= userName)
           
           if created:
              u.set_password(userPass)
              u.save()
              UserScore.objects.create(user=u,points=0)
              uc= UserContact.objects.create(user=u)
              if instagram: uc.instagram = instagram
              uc.save()


              login(request,u)

              return redirect("/desk") 
           else:
              return render(request,  'accounts/register.html', {"m": "El usuario existe", "c":"red"})
        else:
              return render(request,  'accounts/register.html', {"m": "Introduzca password o usuario valido", "c":"red"})

    return render(request,  'accounts/register.html', {"r": ''})

