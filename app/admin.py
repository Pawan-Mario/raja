from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
class UserModel(UserAdmin):
    list_display = ['username','user_type']


admin.site.register(CustomUser, UserModel)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Show)
admin.site.register(Aboutus)
admin.site.register(Leadership)
admin.site.register(Events)
admin.site.register(Gallery)
admin.site.register(Contectinfo)
admin.site.register(LogoF)
admin.site.register(Gslider)

# Register your models here.
