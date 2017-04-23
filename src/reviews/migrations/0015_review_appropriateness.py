# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-10 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0014_auto_20160326_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='appropriateness',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, help_text='Administrators can use this field to hide a review from submitters, even if the reviewer enables disclosure. The review may be shown to the submitter only if this is set to True.', verbose_name='is appropriate'),
        ),
    ]