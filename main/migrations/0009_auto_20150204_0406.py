# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_song_index'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['index']},
        ),
    ]
