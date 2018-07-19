from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile_number = models.IntegerField(null=True)
    email_address = models.CharField(max_length=100)
    client_pic = models.ImageField(upload_to='profile_img', blank=True)

    def __str__(self):
        return self.first_name

