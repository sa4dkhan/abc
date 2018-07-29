from django.db import models


class Lawyer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    speciality = models.TextField(max_length=200)
    mobile_number = models.IntegerField(null=True)
    email_address = models.CharField(max_length=100)
    lawyer_pic = models.ImageField(upload_to='lawyer_img', blank=True)

    def __str__(self):
        return self.first_name

