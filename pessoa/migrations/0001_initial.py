# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastrarPessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(null=True, blank=True, max_length=255)),
                ('apelido', models.CharField(max_length=255)),
                ('sexo', models.CharField(max_length=1, choices=[('M', 'MASCULINO'), ('F', 'FEMININO')])),
                ('datanascimento', models.DateField(verbose_name='Data de Nascimento', null=True, blank=True)),
                ('email', models.EmailField(max_length=255)),
                ('senha', models.CharField(max_length=30)),
                ('endereco', models.CharField(verbose_name='Endereço', null=True, blank=True, max_length=255)),
                ('nro', models.CharField(verbose_name='Número', null=True, blank=True, max_length=255)),
                ('complemento', models.CharField(null=True, blank=True, max_length=255)),
                ('cep', models.CharField(max_length=9)),
                ('bairro', models.CharField(null=True, blank=True, max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('datacadastro', models.DateTimeField(auto_now_add=True)),
                ('tipo_pessoa', models.CharField(verbose_name='Tipo', null=True, blank=True, choices=[('F', 'Pessoa Física'), ('J', 'Pessoa Jurídica')], max_length=1)),
                ('foto', models.ImageField(null=True, upload_to='pessoa/%Y', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False, null=True, blank=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
