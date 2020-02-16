# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("soapbox", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="is_global",
            field=models.BooleanField(
                default=False,
                help_text=("If checked, this message will display on all pages."),
            ),
        ),
    ]
