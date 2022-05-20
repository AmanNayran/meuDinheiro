import py_compile
from re import template
from django.shortcuts import redirect, render
from django.contrib import menssages

from .forms import UsuarioForms

# Create your views here.

def inicio(request):
    return render(request, 'base.html', {})

def novo_usuario(request):
    template_name = 'usuario/novo_usuario.html'
    context = {}
    if request.method == 'POST':
        form = UsuarioForms(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            menssages.success(request, 'Conta criada com sucesso!')
            return redirect('usuarios:login_usuario')
    else:
        form = UsuarioForms()
    context['form'] = form
    return render(request, template_name, context)
    