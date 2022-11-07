"""quiniela URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views as accounts_views
from schedule import views as schedule_views

from .views import home_view, desk_view, admin_manage_view

urlpatterns = [
    path('',  home_view),
    path('desk/',desk_view ),

    path('login/', accounts_views.login_view ),
    path('logout/', accounts_views.logout_view ),
    path('register/', accounts_views.register_view ),

    path('schedule/create/', schedule_views.schedule_create_view),
    
    path('manage/', admin_manage_view),




    path('admin/', admin.site.urls),
]
