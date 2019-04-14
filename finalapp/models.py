#from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from homepage.models import UserProfileInfo
# Create your models herUe.
class Document(models.Model):
    category_choices=(
    ('Objects','Objects'),
    ('Animals','Animals'),
    ('Abstract','Abstract'),
    ('Festivals','Festivals'),
    ('Food','Food'),
    ('Lifestyle','Lifestyle'),
    ('Nature','Nature'),
    ('People','People'),
    ('Architecture','Architecture'),
    ('Sports','Sports'),
    ('Fashion','Fashion'),
    )
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=150,default="")
    category= models.CharField(max_length=150,default="",choices=category_choices)
    image=models.ImageField(default='',upload_to='')
    uploaded_at=models.DateTimeField(auto_now_add=True)

    likes=models.IntegerField(default='0')

    def __str__(self):
        return self.name
    #userid=models.OneToOneField(models1.UserProfileInfo,on_delete='CASCADE')
    #userid=FOREIGNKEY(UserProfileInfo,on_delete='CASCADE')
    #userid = models.ForeignKey(models1.UserProfileInfo,on_delete='CASCADE')

class LikedUser(models.Model):
      user = models.CharField(max_length=100)
      image = models.URLField(max_length=100)

      def __str__(self):
            return str(self.user),str(self.image)
