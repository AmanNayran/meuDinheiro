from django.contrib import messages
from multiprocessing import context
from re import template
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import CategoriaForm
from .models import Categoria

# Create your views here.

@login_required(login_url='/usuarios/login')
def principal(request):
    template_name = 'financas/principal.html'
    context = {}
    return render(request, template_name, context)

def nova_categoria(request):
    template_name = 'financas/nova_categoria.html'
    context = {}
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            cat_form = form.save(commit=False)
            cat_form.usuario = request.user
            cat_form.save()
            messages.success(request, 'Categoria adicionada com sucesso.')
            return redirect('financas:lista_categorias')
    else:
        form = CategoriaForm()
    context['form'] = form
    return render(request, template_name, context)

def lista_categorias(request):
    template_name = 'financas/lista_categorias.html'
    categorias = Categoria.objects.filter(usuario=request.user)
    context = {
        'categorias': categorias
    }
    return render(request, template_name, context)
