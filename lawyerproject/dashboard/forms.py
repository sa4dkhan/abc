from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'mobile_number', 'email_address']


# class ClientForm(forms.Form):
#     First_Name = forms.CharField()
#     Last_Name = forms.CharField()
#     Email_Address = forms.EmailField(label="Email Address")
#     Mobile_Number = forms.NumberInput()
#     # password = forms.CharField(widget=forms.PasswordInput)
#     # password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
#     # first_name = forms.CharField(required=False)
#     # last_name = forms.CharField(required=False)
#     # gender = forms.ChoiceField(choices=((None, ''), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')))
#     # receive_news = forms.BooleanField(required=False, label='I want to receive news and special offers')
#     # agree_toc = forms.BooleanField(required=True, label='I agree with the Terms and Conditions')
#
#     layout = Layout(Fieldset(Row('First_Name', 'Last_Name'),'Email_Address', 'Mobile_Number'))

