from itertools import chain
from django.contrib import messages
from multiprocessing import context
from re import template
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import CategoriaForm, ReceitaForm, DespesaForm
from .models import Categoria, Receita, Despesa

# Create your views here.

@login_required
def principal(request):
    template_name = 'financas/principal.html'
    ultimas_despesas = Despesa.objects.filter(usuario=request.user).order_by('id')[:3]
    ultimas_receitas = Receita.objects.filter(usuario=request.user).order_by('id')[:3]
    ultimas_categorias = Categoria.objects.filter(usuario=request.user).order_by('id')[:3]
    context = {
        'ultimas_despesas': ultimas_despesas,
        'ultimas_receitas': ultimas_receitas,
        'ultimas_categorias': ultimas_categorias,
    }
    return render(request, template_name, context)

# CATEGORIA
@login_required
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

@login_required
def lista_categorias(request):
    template_name = 'financas/lista_categorias.html'
    categorias = Categoria.objects.filter(usuario=request.user)
    context = {
        'categorias': categorias
    }
    return render(request, template_name, context)

@login_required
def editar_categoria(request, pk):
    template_name = 'financas/nova_categoria.html'
    context = {}
    #categoria = get_object_or_404(Categoria, id=pk)
    try:
        categoria = Categoria.objects.get(pk=pk, usuario=request.user)
    except Categoria.DoesNotExist as e:
        messages.warning(request, 'Você não tem permissão para editar a categoria informada.')
        return redirect('financas:lista_categorias')

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria atualizada com sucesso.')
            return redirect('financas:lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    context['form'] = form
        
    return render(request, template_name, context)

@login_required
def apagar_categoria(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk, usuario=request.user)
        categoria.delete()
    except Categoria.DoesNotExist as e:
        messages.warning(request, 'Você não tem permissão para apagar a categoria informada.')
        return redirect('financas:lista_categorias')
    messages.info(request, 'Categoria apagada.')
    return redirect('financas:lista_categorias')

# RECEITA
@login_required
def nova_receita(request):
    template_name = 'financas/nova_receita.html'
    context = {}
    if request.method == 'POST':
        form = ReceitaForm(data=request.POST, user=request.user)
        if form.is_valid():
            receita_form = form.save(commit=False)
            receita_form.usuario = request.user
            receita_form.save()
            messages.success(request, 'Receita adicionada com sucesso.')
            return redirect('financas:lista_receitas')
    else:
        form = ReceitaForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)

@login_required
def lista_receitas(request):
    template_name = 'financas/lista_receitas.html'
    receitas = Receita.objects.filter(usuario=request.user)
    context = {
        'receitas': receitas
    }
    return render(request, template_name, context)

@login_required
def editar_receita(request, pk):
    template_name = 'financas/nova_receita.html'
    context = {}
    try:
        receita = Receita.objects.get(pk=pk, usuario=request.user)
    except Receita.DoesNotExist as e:
        messages.warning(request, 'Você não tem permissão para editar a receita informada.')
        return redirect('financas:lista_receitas')

    if request.method == 'POST':
        form = ReceitaForm(data=request.POST, user=request.user, instance=receita)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receita atualizada com sucesso.')
            return redirect('financas:lista_receitas')
    else:
        form = ReceitaForm(user=request.user, instance=receita)
    context['form'] = form
        
    return render(request, template_name, context)

@login_required
def apagar_receita(request, pk):
    try:
        receita = Receita.objects.get(pk=pk, usuario=request.user)
        receita.delete()
    except Receita.DoesNotExist as e:
        messages.warning(request, 'Você não tem permissão para apagar a receita informada.')
        return redirect('financas:lista_receitas')
    messages.info(request, 'Receita apagada.')
    return redirect('financas:lista_receitas')

# DESPESA
@login_required
def nova_despesa(request):
    template_name = 'financas/nova_despesa.html'
    context = {}
    if request.method == 'POST':
        form = DespesaForm(data=request.POST, user=request.user)
        if form.is_valid():
            despesa_form = form.save(commit=False)
            despesa_form.usuario = request.user
            despesa_form.save()
            messages.success(request, 'Despesa adicionada com sucesso.')
            return redirect('financas:lista_despesas')
    else:
        form = DespesaForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)

@login_required
def lista_despesas(request):
    template_name = 'financas/lista_despesas.html'
    despesas = Despesa.objects.filter(usuario=request.user)
    context = {
        'despesas': despesas
    }
    return render(request, template_name, context)

@login_required
def editar_despesa(request, pk):
    template_name = 'financas/nova_despesa.html'
    context = {}
    try:
        despesa = Despesa.objects.get(pk=pk, usuario=request.user)
    except Despesa.DoesNotExist as e:
        messages.warning(request, 'Você não tem permissão para editar a despesa informada.')
        return redirect('financas:lista_despesas')

    if request.method == 'POST':
        form = DespesaForm(data=request.POST, user=request.user, instance=despesa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Despesa atualizada com sucesso.')
            return redirect('financas:lista_despesas')
    else:
        form = DespesaForm(user=request.user, instance=despesa)
    context['form'] = form
        
    return render(request, template_name, context)

@login_required
def apagar_despesa(request, pk):
    try:
        despesa = Despesa.objects.get(pk=pk, usuario=request.user)
        despesa.delete()
    except Despesa.DoesNotExist as e:
        messages.warning(request, 'Você não tem permissão para apagar a despesa informada.')
        return redirect('financas:lista_despesas')
    messages.info(request, 'Despesa apagada.')
    return redirect('financas:lista_despesas')

# RESULTADO
@login_required
def buscar(request):
    template_name = 'financas/busca_resultados.html'
    context = {}
    termo = request.GET.get('termo', None)
    if termo is not None:
        categorias = Categoria.objects.busca(termo=termo, usuario=request.user)
        receitas = Receita.objects.busca(termo=termo, usuario=request.user)
        despesas = Despesa.objects.busca(termo=termo, usuario=request.user)
        context['categorias'] = categorias
        context['receitas'] = receitas
        context['despesas'] = despesas
    return render(request, template_name, context)

# RELATÓRIO
@login_required
def relatorios(request):
    template_name = 'financas/relatorios.html'
    context = {}
    data_inicial = request.GET.get('data_inicial', None)
    data_final = request.GET.get('data_final', None)
    tipo = request.GET.get('tipo', None)
    if data_inicial and data_final:
        if tipo and tipo == 'RC':
            receitas = Receita.objects.filter(cadastrada_em__gte=data_inicial, cadastrada_em__lte=data_final)
            context = {
                'receitas': receitas
            }
        else:
            despesas = Despesa.objects.filter(cadastrada_em__gte=data_inicial, cadastrada_em__lte=data_final)
            context = {
                'despesas': despesas
            }
    
    return render(request, template_name, context)

# tipo