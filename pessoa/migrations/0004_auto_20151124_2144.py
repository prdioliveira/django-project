# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_auto_20151124_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrarpessoa',
            name='email',
            field=models.EmailField(unique=True, max_length=255),
        ),
    ]
