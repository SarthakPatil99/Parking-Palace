from cgi import print_exception
from distutils.command.upload import upload
from email.policy import default
import profile
from pyexpat import model
from django.db import models
from django.dispatch import receiver
from matplotlib import image
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Users(models.Model):
    username    = models.CharField(max_length=50, default='')
    user_id     = models.AutoField
    user_fname  = models.CharField(max_length=50)
    user_mname  = models.CharField(max_length=50)
    user_lname  = models.CharField(max_length=50)
    user_email  = models.CharField(max_length=50)
    user_phone  = models.IntegerField()
    user_Pname  = models.CharField(max_length=50, default='')
    user_PAname = models.CharField(max_length=50, default='')
    user_Paddr  = models.TextField(default='')
    user_Pimage = models.ImageField(null=True, blank=True, 
    upload_to="home/images/",  default="home/images/row1.jpg")
    # user_slots = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Booking(models.Model):
    O_Username  = models.CharField(max_length=50, default='')
    U_Username  = models.CharField(max_length=50, default='')
    U_FirstName = models.CharField(max_length=50)
    U_LastName  = models.CharField(max_length=50)
    U_MobNo     = models.IntegerField()
    U_Email     = models.CharField(max_length=50)
    U_VehicleNo = models.CharField(max_length=50)
    U_TimeSlot  = models.TimeField(default='00:00')
    U_Duration  = models.TimeField(default='00:00')
    U_token     = models.CharField(max_length=10)
    U_status    = models.BooleanField(default=False)
    U_VType     = models.CharField(max_length=4, default='')
    extended    = models.BooleanField(default=False)
    price       = models.IntegerField(default=0)

    def __str__(self):
        return self.O_Username

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     isOwner = models.CharField(max_length=10)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()