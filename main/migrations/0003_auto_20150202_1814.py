# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150202_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='height',
            new_name='cover_art_height',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='width',
            new_name='cover_art_width',
        ),
        migrations.AddField(
            model_name='album',
            name='synopsis',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
