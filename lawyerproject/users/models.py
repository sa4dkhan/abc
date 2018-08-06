from django.db import models
from role.models import Role

# Create your models here.


class User(models.Model):
    role = models.ForeignKey(Role, related_name='User', on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    status = models.IntegerField(blank=True,null=True)
    created_by = models.IntegerField(blank=True,null=True)
    created_at = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.full_name

