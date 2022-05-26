from cProfile import label
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']


class UsuarioLogin(forms.Form):
    usuario = forms.CharField(label='Usuário', required=True, widget=forms.TextInput(attrs={'class': 'fork-control'}))
    senha = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput(attrs={'class': 'fork-control'}))
