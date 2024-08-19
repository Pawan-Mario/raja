"""
URL configuration for Bappa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from .import views,Hod_Views,User_Views
from Bappa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/',views.Client, name='client'),
    path('login/',views.Login, name='login'),
    path('doLogin/',views.doLogin, name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),
    path('',views.Index, name='index'),
    path('about_us/',views.AboutUs,name='about_us'),
    path('leadership/',views.LeaderShip,name='leadership'),
    path('gallery/',views.Ggallery,name='gallery'),
    path('event/',views.Event,name='event'),
    path('contact_us/',views.ContactUs,name='contact_us'),
    path('',views.ContactInfo,name='contact'),
    path('',views.Logof,name='LogoN'),



    #Profile Url
    path('profile/',views.Profile,name='profile'),
    path('profile/update',views.Profile_Update,name='profile_update'),



    # This is HOD Urls
    path('Hod/Home',Hod_Views.Home,name='hod_home'),
    path('Hod/Add_User',Hod_Views.Add_User,name='add_user'),
    path('Hod/View_User',Hod_Views.View_User,name='view_user'),
    path('Hod/Edit_User/<str:id>',Hod_Views.Edit_User,name='edit_user'),
    path('Hod/Update_User',Hod_Views.Update_User,name='update_user'),
    path('Hod/Delete_User<str:id>',Hod_Views.Delete_User,name='delete_user'),

    # This is User urls
    path('User/Home',User_Views.User_Home,name='user_home'),
    path('User/View_Banner',User_Views.View_Banner,name='view_banner'),
    path('User/Add_Banner',User_Views.Add_Banner,name='add_banner'),
    path('User/Edit_Banner/<str:id>',User_Views.Edit_Banner,name='edit_banner'),
    path('User/Update_Banner',User_Views.Update_Banner,name='update_banner'),
    path('User/Delete_Banner<str:id>',User_Views.Delete_Banner,name='delete_banner'),
    # This is main banner page
    path('User/Main_Banner',User_Views.Main_Banner,name='main_banner'),
    path('User/Add_Main_Banner',User_Views.Add_Main_Banner,name='add_main_banner'),
    path('User/Edit_Main_Banner/<str:id>',User_Views.Edit_Main_Banner,name='edit_main_banner'),
    path('User/Update_Main_Banner',User_Views.Update_Main_Banner,name='update_main_banner'),
    path('User/Delete_Main_Banner<str:id>',User_Views.Delete_Main_Banner,name='delete_main_banner'),
    # This is About us page
    path('User/About_Us',User_Views.User_Aboutus,name='user_about_us'),
    path('User/Edit_About_Us/<str:id>',User_Views.Edit_Aboutus,name='edit_about_us'),
    path('User/Update_About_Us',User_Views.Update_Aboutus,name='update_about_us'),
    # This is Leadership Page
    path('User/Leadership',User_Views.User_Leadership,name='user_leadership'),
    path('User/Add_Leadership',User_Views.Add_Leadership,name='add_leadership'),
    path('User/Edit_Leadership/<str:id>',User_Views.Edit_Leadership,name='edit_leadership'),
    path('User/Update_Leadership',User_Views.Update_Leadership,name='Update_leadership'),
    path('User/Delete_Leadership/<str:id>',User_Views.Delete_Leadership,name='Delete_leadership'),
    # This is Gallery Page
    path('User/Gallery',User_Views.User_Gallery,name='user_gallery'),
    path('User/Add_Gallery',User_Views.Add_Gallery,name='add_gallery'),
    path('User/Edit_Gallery/<str:id>',User_Views.Edit_Gallery,name='edit_gallery'),
    path('User/Update_Gallery',User_Views.Update_Gallery,name='update_gallery'),
    path('User/Delete_Gallery/<str:id>',User_Views.Delete_Gallery,name='delete_gallery'),
    # This is Event Page
    path('User/Event',User_Views.User_Events,name='user_event'),
    path('User/Add_Event',User_Views.Add_Events,name='add_event'),
    path('User/Edit_Event/<str:id>',User_Views.Edit_Events,name='edit_event'),
    path('User/Update_Event',User_Views.Update_Events,name='update_event'),
    path('User/Delete_Event/<str:id>',User_Views.Delete_Events,name='delete_event'),
    # This is Contact Us Page
    path('User/Info',User_Views.User_Info,name='user_contact_us'),
    path('User/Edit_Info/<str:id>',User_Views.Info_Edit,name='edit_info'),
    path('User/Update_Info',User_Views.Update_Info,name='update_info'),
    # This is Header Logo
    path('User/Logo',User_Views.User_Logo,name='user_logo'),
    path('User/Edit_Logo/<str:id>',User_Views.Logo_Edit,name='edit_logo'),
    path('User/Update_Logo',User_Views.Update_Logo,name='update_logo'),
    # This for Gallery Crousal
    path('User/Crousal',User_Views.Crousal,name='crousal'),
    path('User/Add_Crousal',User_Views.Add_Crousal,name='add_crousal'),
    path('User/Edit_Crousal/<str:id>',User_Views.Crousal_Edit,name='edit_crousal'),
    path('User/Update_Crousal',User_Views.Update_Crousal,name='update_crousal'),
    path('User/Delete_Crousal/<str:id>',User_Views.Delete_Crousal,name='delete_crousal'),


    
  





    
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
