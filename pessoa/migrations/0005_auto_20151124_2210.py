# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0004_auto_20151124_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrarpessoa',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
