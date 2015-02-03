# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150203_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='art',
            field=models.ImageField(default='', height_field='art_height', upload_to='song_art', width_field='art_width'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='art_height',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='art_width',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
    ]
