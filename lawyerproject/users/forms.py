from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('role', 'full_name', 'email', 'password', 'status')
