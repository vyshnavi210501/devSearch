from django.dispatch import receiver
from .models import *
from django.db.models.signals import post_delete,post_save
from django.core.mail import send_mail
from django.conf import settings

# @receiver(post_save,sender=Profile)
def createProfile(sender,instance,created,**kwargs):
    if created:
        print("creating profile!")
        user=instance
        profile=Profile.objects.create(user=user,username=user.username,name=user.first_name,email=user.email)
        subject="Welcome to Devsearch!"
        message="We are glad u hv"
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
        )


def deleteUser(sender,instance,**kwargs):
    user=instance.user
    user.delete()

def updateUser(sender,instance,created,**kwargs):
    profile=instance
    user=profile.user
    if created==False:
        user.first_name=profile.name
        user.username=profile.username
        user.email=profile.email
        user.save()

post_save.connect(createProfile,sender=User)
post_save.connect(updateUser,sender=Profile)
post_delete.connect(deleteUser,sender=Profile)