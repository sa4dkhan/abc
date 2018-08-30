from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    phone = models.PositiveIntegerField(blank=True, null=True)
    address = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        user = instance
        if created:
            profile = Profile(user=user)
            profile.save()


    def __str__(self):
        return self.user.username



