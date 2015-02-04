# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150203_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='index',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
