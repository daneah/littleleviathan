# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150202_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover_art',
            field=models.ImageField(width_field='cover_art_width', height_field='cover_art_height', upload_to='cover_art'),
            preserve_default=True,
        ),
    ]
