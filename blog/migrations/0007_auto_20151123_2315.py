# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20151028_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 24, 1, 15, 24, 861912, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(null=True, blank=True, default=datetime.datetime(2015, 11, 24, 1, 15, 24, 861969, tzinfo=utc)),
        ),
    ]
