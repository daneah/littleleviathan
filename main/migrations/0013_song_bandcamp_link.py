# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_song_soundcloud_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='bandcamp_link',
            field=models.URLField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
