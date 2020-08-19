from django.db import models
from django.conf import settings
from uuid import uuid4
import os


def path_and_rename(instance,filename):
    fn, ext = os.path.splitext(filename)
    return "media/userPic/{id}{ext}".format(id=instance.pk, ext=ext)

class Profile(models.Model):
        user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
        photo = models.ImageField(upload_to=path_and_rename,blank=True,null=True)