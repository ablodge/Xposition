# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 15:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_auto_20170819_0708'),
        ('metadata', '0007_auto_20170819_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadatarevision',
            name='article_revision',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='metadata_revision', to='wiki.ArticleRevision'),
            preserve_default=False,
        ),
    ]
