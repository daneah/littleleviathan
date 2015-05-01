# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20150402_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='soundcloud_link',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
