
from django import forms
from django.core.exceptions import ValidationError

from role.models import Role
class RoleForm(forms.Form):
     role_name = forms.CharField(required=True,initial='add')

     def clean_role_name(self):
          role_name = self.cleaned_data['role_name']
          if Role.objects.filter(role_name=role_name).exists():
               raise ValidationError("The role name already taken .")
          return role_name

