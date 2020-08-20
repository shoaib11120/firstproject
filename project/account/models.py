from django.core.files.storage import FileSystemStorage
from django.db import models
from django.conf import settings
from uuid import uuid4
import os


#change image name
def path_and_rename(instance,filename):
	upload_to='userpic/{}'.format(instance.user.username)
	ext=filename.split('.')[-1]
	print(instance.pk)
	filename='{}.{}'.format("profilePic",ext)
	return os.path.join(upload_to,filename)


class OverwriteStorage(FileSystemStorage,):
    def get_available_name(self, name, max_length=None):
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

class Profile(models.Model):
        user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
        photo = models.ImageField(upload_to=path_and_rename,blank=True,null=True,storage=OverwriteStorage())