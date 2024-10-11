from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save




class Profiles(models.Model):
    GENDER_CHOICES=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    user=models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    phone=models.IntegerField(blank=True,null=True)
    Avatar=models.ImageField(default='default_pic.jpg', blank=True, null=True)
    location=models.CharField(max_length=20,blank=True, null=True)
    gender=models.CharField(max_length=6, choices=GENDER_CHOICES,default='Male')
    bio=models.TextField(blank=True, null=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    follows=models.ManyToManyField('self',related_name='followed_by', symmetrical=False,blank=True)
    def __str__(self):
        return self.user.username

def create_profile(sender,instance,created,**kwargs):
    if created:
        user_profile=Profiles(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profiles.id])
        user_profile.save()
post_save.connect(create_profile,sender=User)


class Blogs(models.Model):
    
    user=models.ForeignKey(User,related_name="posts",null=True, on_delete=models.DO_NOTHING)
    post=models.TextField(blank=True, null=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)



    
#python manage.py runserver
#python manage.py makemigrations
#python manage.py migrate