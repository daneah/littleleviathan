# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150202_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='art',
            field=models.ImageField(null=True, width_field='art_width', upload_to='song_art', blank=True, height_field='art_height'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='song',
            name='art_height',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='song',
            name='art_width',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
