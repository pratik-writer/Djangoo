from django.db import models
from django.contrib.auth import get_user_model


User=get_user_model()

class user_profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    bio=models.TextField()
    profileimage=models.ImageField(upload_to='profile_images',default='blank-profile-picture.png')

    def _str_(self):
        return self.user.username;