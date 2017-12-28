# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-02 16:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50, null=True)),
                ('cat_bd', models.DateField(null=True)),
                ('cat_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cats',
                'verbose_name': 'Cat',
            },
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog_name', models.CharField(max_length=50, null=True)),
                ('dog_bd', models.DateField(null=True)),
                ('dog_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dog_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Dogs',
                'verbose_name': 'Dog',
            },
        ),
    ]
