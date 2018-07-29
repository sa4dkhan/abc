from django.db import models
from django.contrib.auth.models import User
from role.models import Role


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)



    #additional info
    phone = models.PositiveIntegerField(blank=True)
    address = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    role_id = models.ForeignKey(Role, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username

