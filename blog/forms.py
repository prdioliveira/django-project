# -*- coding:utf-8 -*-
from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'publish_date')

        labels = {
            'title': ('Título'),
            'text': ('Texto'),
            'publish_date': ('Data de publicação'),
        }

        widgets = {
            'publish_date': AdminSplitDateTime,
        }