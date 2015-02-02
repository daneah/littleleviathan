# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='code',
            field=models.SlugField(max_length=20, default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='code',
            field=models.SlugField(max_length=20, default='test'),
            preserve_default=False,
        ),
    ]
