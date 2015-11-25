# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.admin import User

CHOICE_SEXO = (('M', 'Masculino'), ('F', 'Feminino'), )
CHOICE_TPESSOA = (('F', u'Pessoa Física'), ('J', u'Pessoa Jurídica'), )

class CadastrarPessoa(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, editable=False)

    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, null=True, blank=True)
    apelido = models.CharField(max_length=255)
    sexo = models.CharField(max_length=1, choices=CHOICE_SEXO)
    datanascimento = models.DateField(verbose_name='Data de Nascimento', blank=True, null=True)
    email = models.EmailField(max_length=255)
    senha = models.CharField(max_length=30)
    endereco = models.CharField(max_length=255, verbose_name='Endereço', blank=True, null=True)
    nro = models.CharField(max_length=255, verbose_name='Número', blank=True, null=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    datacadastro = models.DateTimeField(auto_now_add=True)
    tipo_pessoa = models.CharField(max_length=1, verbose_name='Tipo', choices=CHOICE_TPESSOA, blank=True, null=True)
    foto = models.ImageField(upload_to='pessoa/%Y', null=True, blank=True)

    class Meta:
        ordering = ['-id']


    def save(self):
        if not self.id:
            c = CadastrarPessoa.objects.filter(email=self.email).count()
            if c:
                print('Email já existe', CadastrarPessoa.email)

            usr = User.objects.filter(username = self.email)
            print('USR >>>', usr)
            print('EMAIL >>>>', self.email)

            if usr:
                u = usr[0]
                print('USR[0] >>>', usr[0])

            else:
                u = User.objects.create_user(self.email, self.email, self.senha)
                print('User >>> ', u)
            u.save()
            self.user = u

            print('Self.user >>>', self.user)

        else:
            self.user.username = self.email
            self.user.email = self.email
            self.user.set_apssword(self.senha)
            self.user.save()
        super(CadastrarPessoa, self).save()


    def __str__(self):
        return self.email
