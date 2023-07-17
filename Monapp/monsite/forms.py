from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Client
        fields = ( 'first_name', 'last_name' , 'username', 'password', 'numeroTel', 'datenaissance_client','email_client','adresse_client')