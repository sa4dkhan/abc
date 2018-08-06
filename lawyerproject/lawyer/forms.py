from django import forms
from .models import Lawyer
from simple_search import search_form_factory

SearchForm = search_form_factory(Lawyer.objects.all(),
                                 ['^first_name', 'last_name', 'speciality'])


class LawyerForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        fields = ['first_name', 'last_name', 'speciality', 'lawyer_pic', 'mobile_number', 'email_address']



