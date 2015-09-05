# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('message',
                 models.TextField()),
                ('is_global',
                 models.BooleanField(
                     help_text=(b'If checked, this message will '
                                b'display on all pages.'))),
                ('is_active',
                 models.BooleanField(
                     default=True,
                     help_text=b'Only active messages will be displayed.')),
                ('url',
                 models.CharField(
                     help_text=(b'Message will be displayed on any URL '
                                b'which matches this.'),
                     max_length=255,
                     null=True,
                     verbose_name=b'URL',
                     blank=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
