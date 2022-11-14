from django.shortcuts import render
from django.contrib.auth.models import Group, User
  

# Create your views here.
def group_create_view (request): 
    print(request.POST)

    if request.method == "POST":
        group, created = Group.objects.get_or_create(name=request.POST.get('group_name'))
        if request.POST.get('include') and created:
            user = request.user 
            user.groups.add(group)
        
    users = group.user_set.all()
    context = {
        "group" : group,
        "created": created,
        "users": users 
    }

    



            
    print(created)
    return render(request, 'group/create.html', context)



def group_manage_view (request): 
    user = request.user 
    user_groups = user.groups.all()
    other_groups = Group.objects.exclude(user=user)
    
    context  = {
        "user_groups" : user_groups,
        "groups" : other_groups, 
    }
    return render(request, 'group/manage.html', context )

def group_include_view (request): 
    if request.method == "POST":
            group = Group.objects.get(name = request.POST.get('group_name'))
            user = request.user 
            user.groups.add(group)

    users = group.user_set.all()
    context = {
        "group" : group,
        "users": users 
    }


    return render(request, 'group/include.html', context )


def group_exclude_view (request): 
    if request.method == "POST":
            group = Group.objects.get(name = request.POST.get('group_name'))
            user = request.user 
            user.groups.remove(group)
    context = {
        "group" : group
            }

    return render(request, 'group/exclude.html', context )