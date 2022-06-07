from django.db import models
from django.db.models import Q

class CategoriaManager(models.Manager):

    def busca(self, termo=None, usuario=None):
        qs = self.get_queryset()
        if termo is not None and usuario is not None:
            or_lockup = (Q(nome__icontains=termo) | Q(descricao__icontains=termo))
        qs = qs.filter(or_lockup, usuario__username=usuario).distinct()
        return qs

class ReceitaManager(models.Manager):

    def busca(self, termo=None, usuario=None):
        qs = self.get_queryset()
        if termo is not None and usuario is not None:
            or_lockup = (Q(categoria__nome__icontains=termo) | Q(descricao__icontains=termo))
        qs = qs.filter(or_lockup, usuario__username=usuario).distinct()
        return qs

class DespesaManager(models.Manager):

    def busca(self, termo=None, usuario=None):
        qs = self.get_queryset()
        if termo is not None and usuario is not None:
            or_lockup = (Q(categoria__nome__icontains=termo) | Q(identificacao__icontains=termo) | Q(descricao__icontains=termo))
        qs = qs.filter(or_lockup, usuario__username=usuario).distinct()
        return qs
