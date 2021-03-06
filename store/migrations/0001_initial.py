# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('shine', models.IntegerField()),
                ('price', models.FloatField()),
                ('rarity', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('faces', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('body', models.CharField(blank=True, max_length=250)),
                ('author', models.CharField(max_length=50)),
                ('createdOn', models.DateField()),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='store.Product')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.Product'),
        ),
    ]
