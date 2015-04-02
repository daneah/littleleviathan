# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_song_duration_seconds'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='itunes_link',
            field=models.URLField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='song',
            name='itunes_link',
            field=models.URLField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
