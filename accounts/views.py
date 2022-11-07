from django.shortcuts import render
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
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
    print(request.user)
    return render(request,  'accounts/login.html', {})
    
def logout_view (request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    return render(request,  'accounts/logout.html', {})

