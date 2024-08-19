from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER = (
        (1,'HOD'),
        (2,'User1'),
    )
    user_type = models.CharField(choices=USER,max_length=50,default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')



    
# Create your models here.
class Category(models.Model):
 name = models.CharField(max_length=200)

def __str__(self):
    return self.name

class Post(models.Model):
    STATUS = (
        ('0', 'Draft'),
        ('1', 'Publish'),
    )
    SECTION = (
        ('news','news'),
        ('product','product'),
        ('event','event'),
    )

    feured_image = models.ImageField(upload_to='Images')
    title = models.CharField(max_length=200)
    content = RichTextField()
    status = models.CharField(choices=STATUS,max_length=100)
    section = models.CharField(choices=SECTION,max_length=200)

    def __str__(self):
        return self.title
class Show(models.Model):
   STATUS = (
        ('0','Draft'),
        ('1','Publish'),
    )
   SECTION = (
      ('banner','banner'),
      ('gallery','gallery'),
    )
   feured_image = models.ImageField(upload_to='Images')
   status = models.CharField(choices=STATUS,max_length=100)
   section = models.CharField(choices=SECTION,max_length=200)
   def __str__(self):
        return self.section

class Aboutus(models.Model):
    feured_image = models.ImageField(upload_to='Images')
    title = models.CharField(max_length=200)
    content = RichTextField()
    def __str__(self):
        return self.title
   
   
class Leadership(models.Model):
    feured_image = models.ImageField(upload_to='Images')
    title = models.CharField(max_length=200)
    content = RichTextField()
    def __str__(self):
        return self.title

class Gallery(models.Model):
    feured_image = models.ImageField(upload_to='Images')
    imageq = models.ImageField(upload_to='Images')
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Events(models.Model):
    feured_image = models.ImageField(upload_to='Images')
    title = models.CharField(max_length=200)
    content = RichTextField()
    def __str__(self):
        return self.title
    
class Contectinfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    youtube = models.CharField(max_length=200)
    linkdin = models.CharField(max_length=200)
    def __str__(self):
        return self.email

class LogoF(models.Model):
    feured_image = models.ImageField(upload_to='Images')
    def __str__(self):
        return str(self.feured_image)
    

class Gslider(models.Model):
    document = models.FileField(upload_to='doc/')
    imageq = models.ImageField(upload_to='Images')
    def __str__(self):
        return str(self.document.name)