# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("message", models.TextField()),
                (
                    "is_global",
                    models.BooleanField(
                        help_text=(
                            "If checked, this message will display on all pages."
                        )
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Only active messages will be displayed.",
                    ),
                ),
                (
                    "url",
                    models.CharField(
                        help_text=(
                            "Message will be displayed on any URL which matches this."
                        ),
                        max_length=255,
                        null=True,
                        verbose_name="URL",
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
    ]
