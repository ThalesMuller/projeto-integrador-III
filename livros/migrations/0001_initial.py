# Generated by Django 5.0.4 on 2024-04-29 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('isbn', models.CharField(max_length=13)),
                ('titulo', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=100)),
                ('editora', models.CharField(max_length=100)),
                ('ano_publicacao', models.IntegerField()),
                ('numero_paginas', models.IntegerField()),
                ('rating', models.FloatField()),
                ('created_at', models.DateField()),
                ('created_by', models.IntegerField()),
            ],
        ),
    ]
