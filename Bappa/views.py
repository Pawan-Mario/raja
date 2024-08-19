from django.shortcuts import render, redirect, HttpResponse
from app.models import Gslider, Post,Show,Aboutus,Leadership,Gallery,Events,Contectinfo,LogoF

from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser
from django.core.mail import send_mail
from django.conf import settings



def Client(request):
    return render(request,'client.html')

def Index(request):
    image = LogoF.objects.all()
    info = Contectinfo.objects.all()
    news_post = Post.objects.filter(section='news').order_by('-id')[0:1]
    product_post = Post.objects.filter(section='product').order_by('-id')[0:6]
    event_post = Post.objects.filter(section='event').order_by('-id')[0:3]
    banner_post = Show.objects.filter(section='banner').order_by('-id')[0:3]
    gallery_post = Show.objects.filter(section='gallery').order_by('-id')[0:8]
    

    context={
        'image':image,
        'info':info,
        'banner_post':banner_post,
        'gallery_post':gallery_post,
        'news_post':news_post,
        'product_post':product_post,
        'event_post':event_post,


    }
    return render(request,'index.html',context)
def Login(request):
    return render(request,'login.html')
def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'),)
        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return redirect('user_home')
            else:
                messages.error(request, 'Email and Password are Invalid !')
                return redirect('login')
        else:
            messages.error(request, 'Email and Password are Invalid !')
            return redirect('login')


def doLogout(request):
    logout(request)
    return redirect('login')
    
def AboutUs(request):
    image = LogoF.objects.all()
    info = Contectinfo.objects.all()
    user_about_us = Aboutus.objects.all().order_by('-id')[0:1]
    context = {
        'image':image,
        'info':info,
        'user_about_us':user_about_us
        }
    return render(request,'about_us.html',context)

def LeaderShip(request):
    image = LogoF.objects.all()
    info = Contectinfo.objects.all()
    leadership = Leadership.objects.all().order_by('-id')[0:6]
    context = {
        'image':image,
        'info':info,
        'leadership':leadership
        }
    return render(request,'leadership.html',context)

def Ggallery(request):
    image = LogoF.objects.all()
    info = Contectinfo.objects.all()
    gallery = Gallery.objects.all().order_by('id')
    gslider = Gslider.objects.all()
    context = {
        'image':image,
        'info':info,
        'gallery':gallery,
        'gslider':gslider
        }
    return render(request,'gallery.html',context)

def Event(request):
    image = LogoF.objects.all()
    info = Contectinfo.objects.all()
    events = Events.objects.all().order_by('-id')
    context = {
        'image':image,
        'info':info,
        'events':events
        }
    return render(request,'events.html',context)
    
def ContactUs(request):
    image = LogoF.objects.all()
    email ='kheranicharaja@gmail.com'
    info = Contectinfo.objects.all()
    if request.method == 'POST':
        # email=request.POST['email']
        conemail=request.POST['conemail']
        name=request.POST['name']
        message = request.POST['message']
        phone=request.POST['phone']
        email_message = f"Name: {name}\nEmail: {conemail}\nPhone: {phone}\n\nMessage:\n{message}"
        send_mail(
            'Contact Form',
            email_message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )
    context = {
        'image':image,
        'info':info,
    }
    return render(request,'contact_us.html',context)

def ContactInfo(request):
    info = Contectinfo.objects.all()
    return render(request,'footer.html',{'info':info,})

def Logof(request):
    image = LogoF.objects.all()
    return render(request,'header.html',{'image':image,})

@login_required(login_url='/')
def Profile(request):
    user = CustomUser.objects.get(id = request.user.id)
    
    context = {
        "user":user,
    }
    return render(request,'profile.html',context)

@login_required(login_url='/')
def Profile_Update(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        # username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id = request.user.id)

            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.profile_pic = profile_pic

            if password !=None and password != "":
                customuser.set_password(password)
            if profile_pic !=None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request,'Your Profile Updated Successfully')
            return redirect('profile')
        
        
        except:
            messages.error(request,'Your Profile is not Updated')


    return render(request,'profile.html')