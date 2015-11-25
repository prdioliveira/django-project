# -*- coding:utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.admin import User
from .models import CadastrarPessoa

class CadastrarPessoaForm(forms.ModelForm):
    class Meta:
        model = CadastrarPessoa

        fields = (
            'nome',
            'sobrenome',
            'apelido',
            'sexo',
            'datanascimento',
            'email',
            'senha',
            'cep',
            'endereco',
            'nro',
            'bairro',
            'cidade',
            'estado',
            'tipo_pessoa',
            'foto'
        )

        widgets = {
            'senha': forms.PasswordInput,
        }


    def clean_email(self):
        email = self.cleaned_data['email']
        print('Email:', email)
        number_occurrences = User.objects.filter(email=email).count()
        print('Usuario:', User.objects.filter(email=email))
        print('Numero de Ocorrencias:', number_occurrences)
        if  number_occurrences > 0:
            raise ValidationError(u'Email Já cadastrado')
        return self.cleaned_data['email']