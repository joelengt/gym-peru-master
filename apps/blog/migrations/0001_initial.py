# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-29 01:18
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=250)),
                ('slug', models.SlugField(help_text='No llenar, este campo se llena solo')),
                ('frase', models.CharField(max_length=250)),
                ('imagen_frase', models.ImageField(upload_to='fraseimagen')),
                ('fecha', models.DateField(auto_now=True)),
                ('categoria', models.CharField(choices=[('Actualidad', 'Actualidad'), ('Fitnes', 'Fitnes'), ('Nutricion', 'Nutrición')], max_length=40)),
                ('contenido', tinymce.models.HTMLField()),
                ('facebook', models.URLField(blank=True, null=True)),
                ('mas_info', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'ordering': ('-created_at',),
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('imagen', models.ImageField(upload_to='imagenes')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imágenes',
            },
        ),
        migrations.CreateModel(
            name='Ruleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen1', models.ImageField(upload_to='Ruleta')),
                ('imagen2', models.ImageField(upload_to='Ruleta')),
                ('imagen3', models.ImageField(upload_to='Ruleta')),
                ('imagen4', models.ImageField(upload_to='Ruleta')),
            ],
            options={
                'verbose_name': 'Ruleta',
                'verbose_name_plural': 'Ruletas',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='imagenes',
            field=models.ManyToManyField(blank=True, null=True, related_name='imagenes', to='blog.Imagenes'),
        ),
        migrations.AddField(
            model_name='blog',
            name='video',
            field=models.ManyToManyField(blank=True, null=True, related_name='videos', to='blog.Video'),
        ),
    ]
