# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_song_bandcamp_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='bandcamp_link',
            field=models.URLField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='soundcloud_link',
            field=models.URLField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='spotify_link',
            field=models.URLField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='song',
            name='spotify_link',
            field=models.URLField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
