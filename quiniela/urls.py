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
from group import views as group_views
from django.conf import settings
from django.conf.urls.static import static

from .views import home_view, desk_view, admin_manage_view, generate_points, info_view, user_puntuation

urlpatterns = [
    path('',  home_view),
    path('desk/',desk_view ),
    path('info/',info_view ),


    path('login/', accounts_views.login_view ),
    path('logout/', accounts_views.logout_view ),
    path('register/', accounts_views.register_view ),

    #path('schedule/create/', schedule_views.schedule_create_view),
    path('schedule/view/', schedule_views.schedule_view_selections),
    #path('schedule/edit/', schedule_views.schedule_edit_selections),
    path('schedule/group-board/', schedule_views.schedule_group_board_selections),


    path('group/create/', group_views.group_create_view),
    path('group/manage/', group_views.group_manage_view),
    path('group/include/', group_views.group_include_view),
    path('group/exclude/', group_views.group_exclude_view),
    
    path('user/<str:user>/',user_puntuation),







    
    path('manage/', admin_manage_view),
    path('manage/generate-points/', generate_points),


    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
