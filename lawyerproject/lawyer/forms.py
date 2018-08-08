from django import forms
from .models import Lawyer
from dashboard.models import Client
from simple_search import search_form_factory

SearchForm = search_form_factory(Lawyer.objects.all(),
                                 ['^first_name', 'last_name', 'speciality'])
# form = (list(chain(qs1, qs2, qs3))
SearchForm1 = search_form_factory(Client.objects.all(), ['first_name', 'last_name'])


# SearchForm1 = search_form_factory(Client.objects.all(),
#                                  ['^first_name', 'last_name'])


class LawyerForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        fields = ['first_name', 'last_name', 'speciality', 'lawyer_pic', 'mobile_number', 'email_address']



