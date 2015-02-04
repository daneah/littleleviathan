# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150204_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='duration_seconds',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
