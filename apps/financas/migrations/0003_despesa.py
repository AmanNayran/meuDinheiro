# Generated by Django 4.0.4 on 2022-05-26 00:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('financas', '0002_receita'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacao', models.CharField(max_length=100, verbose_name='Identificação')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Valor R$')),
                ('cadastrada_em', models.DateTimeField(auto_now_add=True, verbose_name='Cadastrada em')),
                ('atualizada_em', models.DateTimeField(auto_now=True, verbose_name='Atualizada em')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='financas.categoria', verbose_name='Categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Despesa',
                'verbose_name_plural': 'Despesas',
                'ordering': ['-cadastrada_em'],
            },
        ),
    ]
