# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150203_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='code',
            field=models.SlugField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='code',
            field=models.SlugField(),
            preserve_default=True,
        ),
    ]
