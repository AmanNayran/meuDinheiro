from django import forms
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):

    class Meta:
        modek = User
        fields = ['first_name','last_name','username','email','password']