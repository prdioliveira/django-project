# -*- coding:utf-8 -*-
from django import forms
from django.forms import Textarea
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

        labels = {
            'title': ('Título'),
            'text': ('Texto'),
        }