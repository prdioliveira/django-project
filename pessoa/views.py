# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from .forms import CadastrarPessoaForm
from .models import CadastrarPessoa
from django.utils import timezone

def pessoa_list(request):
    pessoas = CadastrarPessoa.objects.filter(datacadastro__lte=timezone.now()).order_by('-datacadastro')
    return render(request, 'pessoa/pessoa_list.html', {'pessoas': pessoas})

def pessoa_detail(request, pk):
    pessoa = get_object_or_404(CadastrarPessoa, pk=pk)
    return render(request, 'pessoa/pessoa_detail.html', {'pessoa': pessoa})

@login_required(login_url='/login/')
def cad_pessoa(request):
    form = CadastrarPessoaForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('pessoa.views.pessoa_list')
    return render(request, 'pessoa/pessoa_edit.html', {'form': form})

@login_required(login_url='/login/')
def pessoa_edit(request, pk):
    pessoa = get_object_or_404(CadastrarPessoa, pk=pk)
    if request.method == "POST":
        form = CadastrarPessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            pessoa.save()
            return redirect('blog.views.post_detail', pk=pessoa.pk)
    else:
        form = CadastrarPessoaForm(instance=pessoa)
    return render(request, 'blog/post_edit.html', {'form': form})