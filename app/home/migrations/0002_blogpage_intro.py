# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 17:52
from __future__ import unicode_literals

import wagtail.wagtailcore.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='intro',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
