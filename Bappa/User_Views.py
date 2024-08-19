from django.shortcuts import render, redirect, HttpResponse
from app.models import Contectinfo, Gslider, Post,Show,CustomUser,Aboutus,Leadership,Gallery,Events,LogoF
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required(login_url='/')
def User_Home(request):
    return render(request,'client/home.html')

@login_required(login_url='/')
def View_Banner(request):
    post = Post.objects.all()
    context={
        'post':post
    }
    return render(request,'client/first_page.html',context)

@login_required(login_url='/')
def Add_Banner(request):
    sections = Post.objects.all()
    if request.method == "POST":
        feured_image = request.FILES.get('feured_image')
        title = request.POST.get('title')
        content = request.POST.get('content')
        section = request.POST.get('section')
        
        post = Post(
            feured_image=feured_image,
            title=title,
            content=content,
            section=section
        )
        post.save()
        messages.success(request,'User Added Successfully')
        return redirect('view_banner')
    context = {
        'sections': sections,
        'section_choices': Post.SECTION,  # Pass section choices to the template
    }
    return render(request,'client/add_first_page.html',context)

@login_required(login_url='/')
def Edit_Banner(request,id):
    post = Post.objects.filter(id=id)

    context = {
        'post':post,
    }
    return render(request,'client/edit_first_page.html',context)

@login_required(login_url='/')
def Update_Banner(request):
    if request.method == "POST":
        feured_image = request.FILES.get('feured_image')
        title = request.POST.get('title')
        content = request.POST.get('content')
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        if feured_image !=None and feured_image != "":
                post.feured_image = feured_image
        post.title = title
        post.content = content
        post.save()
        messages.success(request,'User Updated Successfully')
        return redirect('view_banner')
    context = {
        'post':post,  
        # 'section_choices':Post.SECTION,  # Pass section choices to the template
    }
    # print()
    return render(request,'client/edit_first_page.html',context)

@login_required(login_url='/')
def Delete_Banner(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    messages.success(request,'User Deleted Successfully')
    return redirect('view_banner')

@login_required(login_url='/')
def Main_Banner(request):
    show = Show.objects.all()
    context={
        'show':show
    }
    return render(request,'main_banner/banner.html',context)

@login_required(login_url='/')
def Add_Main_Banner(request):
    show = Show.objects.all()
    if request.method == "POST":
        feured_image = request.FILES.get('feured_image')
        section = request.POST.get('section')
        
        show = Show(
            feured_image=feured_image,
            section=section
        )
        show.save()
        messages.success(request,'User Added Successfully')
        return redirect('main_banner')
    context = {
        'show': show,
        'section_choices': Show.SECTION,  # Pass section choices to the template
    }
    return render(request,'main_banner/add_banner.html',context)


@login_required(login_url='/')
def Edit_Main_Banner(request,id):
    show = Show.objects.filter(id=id)

    context = {
        'show':show,
    }
    return render(request,'main_banner/edit_banner.html',context)


@login_required(login_url='/')
def Update_Main_Banner(request):
    if request.method == "POST":
        feured_image = request.FILES.get('feured_image')
        show_id = request.POST.get('show_id')
        show = Show.objects.get(id=show_id)
        if feured_image !=None and feured_image != "":
                show.feured_image = feured_image
        show.save()
        messages.success(request,'User Updated Successfully')
        return redirect('main_banner')
    context = {
        'show':show,  
        # 'section_choices':Post.SECTION,  # Pass section choices to the template
    }
    # print()
    return render(request,'main_banner/edit_banner.html',context)

@login_required(login_url='/')
def Delete_Main_Banner(request,id):
    show = Show.objects.get(id=id)
    show.delete()
    messages.success(request,'User Deleted Successfully')
    return redirect('view_banner')

def User_Aboutus(request):
    aboutus = Aboutus.objects.all().order_by('-id')[0:1]
    context = {
        'aboutus': aboutus
    }
    return render(request,'about_us/aboutus.html',context)

@login_required(login_url='/')
def Edit_Aboutus(request,id):
    aboutus = Aboutus.objects.filter(id=id)

    context = {
        'aboutus':aboutus,
    }
    return render(request,'about_us/edit_aboutus.html',context)

@login_required(login_url='/')
def Update_Aboutus(request):
    if request.method == "POST":
        feured_image = request.FILES.get('feured_image')
        title = request.POST.get('title')
        content = request.POST.get('content')
        post_id = request.POST.get('post_id')
        post = Aboutus.objects.get(id=post_id)
        if feured_image !=None and feured_image != "":
                post.feured_image = feured_image
        post.title = title
        post.content = content
        post.save()
        messages.success(request,'User Updated Successfully')
        return redirect('user_about_us')
    return render(request,'about_us/edit_aboutus.html')

@login_required(login_url='/')
def User_Leadership(request):
    leadership = Leadership.objects.all().order_by('-id')[0:6]
    context = {
        'leadership': leadership
    }
    return render(request,'Leadership/leadership.html',context)

@login_required(login_url='/')
def Add_Leadership(request):
    if request.method == "POST":
        feured_image = request.FILES.get('feured_image')
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        post = Leadership(
            feured_image=feured_image,
            title=title,
            content=content,
        )
        post.save()
        messages.success(request,'User Added Successfully')
        return redirect('user_leadership')
    return render(request,'Leadership/add_leadership.html')


@login_required(login_url='/')
def Edit_Leadership(request,id):
    leadership = Leadership.objects.filter(id=id)

    context = {
        'leadership':leadership,
    }
    return render(request,'Leadership/edit_leadership.html',context)

@login_required(login_url='/')
def Update_Leadership(request):
    if request.method == "POST":
        feured_image = request.FILES.get('feured_image')
        title = request.POST.get('title')
        content = request.POST.get('content')
        post_id = request.POST.get('post_id')
        post = Leadership.objects.get(id=post_id)
        if feured_image !=None and feured_image != "":
                post.feured_image = feured_image
        post.title = title
        post.content = content
        post.save()
        messages.success(request,'User Updated Successfully')
        return redirect('user_about_us')
    return render(request,'Leadership/edit_leadership.html')

@login_required(login_url='/')
def Delete_Leadership(request):
    leadership = Leadership.objects.get(id=id)
    leadership.delete()
    messages.success(request,'User Deleted Successfully')
    return redirect('user_leadership')

@login_required(login_url='/')
def User_Gallery(request):
    gallery = Gallery.objects.all().order_by('-id')
    context = {
        'gallery': gallery
    }
    return render(request,'ggallery/gallery.html',context)

@login_required(login_url='/')
def Add_Gallery(request):
    if request.method == "POST":
        feured_image = request.FILES.get('feured_image')
        imageq = request.FILES.get('imageq')
        title = request.POST.get('title')
        
        post = Gallery(
            imageq = imageq,
            feured_image = feured_image,
            title = title,
        )
        post.save()
        messages.success(request,'User Added Successfully')
        return redirect('user_gallery')
    return render(request,'ggallery/add_gallery.html')


@login_required(login_url='/')
def Edit_Gallery(request,id):
    gallery = Gallery.objects.filter(id=id)

    context = {
        'gallery':gallery,
    }
    return render(request,'ggallery/edit_gallery.html',context)

@login_required(login_url='/')
def Update_Gallery(request):
    if request.method == "POST":
        feured_image = request.FILES.get('feured_image')
        imageq = request.FILES.get('imageq')
        title = request.POST.get('title')
        post_id = request.POST.get('post_id')
        post = Gallery.objects.get(id=post_id)
        if feured_image !=None and feured_image != "":
                post.feured_image = feured_image
        post.title = title
        post.imageq = imageq
        post.save()
        messages.success(request,'User Updated Successfully')
        return redirect('user_gallery')
    return render(request,'ggallery/edit_gallery.html')

@login_required(login_url='/')
def Delete_Gallery(request,id):
    gallery = Gallery.objects.get(id=id)
    gallery.delete()
    messages.success(request,'User Deleted Successfully')
    return redirect('user_gallery')

@login_required(login_url='/')
def User_Events(request):
    events = Events.objects.all().order_by('-id')
    context = {
        'events': events
    }
    return render(request,'Event/event.html',context)

@login_required(login_url='/')
def Add_Events(request):
    if request.method == "POST":
        feured_image = request.FILES.get('feured_image')
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        post = Events(
            feured_image=feured_image,
            title=title,
            content=content,
        )
        post.save()
        messages.success(request,'User Added Successfully')
        return redirect('user_event')
    return render(request,'Event/add_event.html')

@login_required(login_url='/')
def Edit_Events(request,id):
    events = Events.objects.filter(id=id)

    context = {
        'events':events,
    }
    return render(request,'Event/edit_event.html',context)

@login_required(login_url='/')
def Update_Events(request):
    if request.method == "POST":
        feured_image = request.FILES.get('feured_image')
        title = request.POST.get('title')
        content = request.POST.get('content')
        post_id = request.POST.get('post_id')
        post = Events.objects.get(id=post_id)
        if feured_image !=None and feured_image != "":
                post.feured_image = feured_image
        post.title = title
        post.content = content
        post.save()
        messages.success(request,'User Updated Successfully')
        return redirect('user_event')
    return render(request,'Event/edit_event.html')

@login_required(login_url='/')
def Delete_Events(request,id):
    events = Events.objects.get(id=id)
    events.delete()
    messages.success(request,'User Deleted Successfully')
    return redirect('user_event')

@login_required(login_url='/')
def User_Info(request):
    info = Contectinfo.objects.all().order_by('-id')
    context = {
        'info': info
    }
    return render(request,'Contactinfo/info.html',context)

@login_required(login_url='/')
def Info_Edit(request,id):
    info = Contectinfo.objects.filter(id=id)

    context = { 
        'info':info,
    }
    return render(request,'Contactinfo/edit_info.html',context)

@login_required(login_url='/')
def Update_Info(request):
    if request.method == "POST":
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        facebook = request.POST.get('facebook')
        twitter = request.POST.get('twitter')
        instagram = request.POST.get('instagram')
        linkdin = request.POST.get('linkdin')
        youtube = request.POST.get('youtube')
        post_id = request.POST.get('post_id')
        post = Contectinfo.objects.get(id=post_id)
        if email !=None and email != "":
                post.email = email
        post.email = email
        post.phone = phone
        post.address = address
        post.facebook = facebook
        post.twitter = twitter
        post.instagram = instagram
        post.linkdin = linkdin
        post.youtube = youtube
        post.save()
        messages.success(request,'Updated Successfully')
        return redirect('user_info')
    return render(request,'Contactinfo/edit_info.html')

@login_required(login_url='/')
def User_Logo(request):
    info = LogoF.objects.all().order_by('-id')
    context = {
        'info': info
    }
    return render(request,'Contactinfo/logo.html',context)

@login_required(login_url='/')
def Logo_Edit(request,id):
    info = LogoF.objects.filter(id=id)

    context = { 
        'info':info,
    }
    return render(request,'Contactinfo/edit_logo.html',context)

@login_required(login_url='/')
def Update_Logo(request):
    if request.method == "POST":
        feured_image = request.FILES.get('feured_image')
        post_id = request.POST.get('post_id')
        post = LogoF.objects.get(id=post_id)
        if feured_image !=None and feured_image != "":
                post.feured_image = feured_image
        post.save()
        messages.success(request,'User Updated Successfully')
        return redirect('user_gallery')
    return render(request,'Contactinfo/edit_logo.html')

@login_required(login_url='/')
def Crousal(request):
     Cro = Gslider.objects.all().order_by('-id')
     context = {
        'Cro': Cro
     }
     return render(request,'ggallery/slider.html',context)

@login_required(login_url='/')
def Add_Crousal(request):
    if request.method == "POST":
        imageq = request.FILES.get('imageq')
        document = request.FILES.get('document')
        
        post = Gslider(
            imageq=imageq,
            document=document,
        )
        post.save()
        messages.success(request,'User Added Successfully')
        return redirect('crousal')
    return render(request,'ggallery/add_slider.html')

@login_required(login_url='/')
def Crousal_Edit(request,id):
    Cro = Gslider.objects.filter(id=id)

    context = { 
        'Cro':Cro,
    }
    return render(request,'ggallery/edit_slider.html',context)

@login_required(login_url='/')
def Update_Crousal(request):
    if request.method == "POST":
        imageq = request.FILES.get('imageq')
        post_id = request.POST.get('post_id')
        post = Gslider.objects.get(id=post_id)
        if imageq !=None and imageq != "":
                post.imageq = imageq
        post.save()
        messages.success(request,'User Updated Successfully')
        return redirect('slider')
    return render(request,'ggallery/edit_slider.html')

@login_required(login_url='/')
def Delete_Crousal(request,id):
    Cro = Gslider.objects.get(id=id)
    Cro.delete()
    messages.success(request,'Deleted Successfully')
    return redirect('crousal')

     


