from django.shortcuts import render, redirect, HttpResponse
from app.models import Post,Show,CustomUser
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required(login_url='/')
def Home(request):
    return render(request,'home.html')

@login_required(login_url='/')
def Add_User(request):
     if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username Already Exists')
            return redirect('add_user')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email Already Exists')
            return redirect('add_user')
        user = CustomUser(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            profile_pic=profile_pic,
            user_type=2
        )
        user.set_password(password)
        user.save()
        messages.success(request,'User Added Successfully')
        return redirect('add_user')

     return render(request,'hod/add_user.html')

@login_required(login_url='/')
def View_User(request):
    users = CustomUser.objects.all()
    context={
        'users':users
    }
    return render(request,'hod/view_user.html',context)

@login_required(login_url='/')
def Edit_User(request,id):
    users = CustomUser.objects.filter(id=id)
    context = {
        'users':users
    }
    return render(request,'hod/edit_user.html',context)

@login_required(login_url='/')
def Update_User(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_id = request.POST.get('user_id')

        user = CustomUser.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if password !=None and password != "":
            user.set_password(password)
            if profile_pic !=None and profile_pic != "":
                user.profile_pic = profile_pic
        user.save()
        messages.success(request,'User Updated Successfully')
        return redirect('view_user')
    return render(request,'hod/edit_user.html')


@login_required(login_url='/')
def Delete_User(request,id):
    user = CustomUser.objects.get(id=id)
    user.delete()
    messages.success(request,'User Deleted Successfully')
    return redirect('view_user')