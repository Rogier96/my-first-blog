# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-20 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='recipe',
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='ingredients',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]