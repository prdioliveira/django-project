# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20151124_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 24, 23, 44, 53, 641260, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(null=True, default=datetime.datetime(2015, 11, 24, 23, 44, 53, 641317, tzinfo=utc), blank=True),
        ),
    ]
