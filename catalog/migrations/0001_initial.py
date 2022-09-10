# Generated by Django 4.0.6 on 2022-08-28 17:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_catalogo', models.CharField(max_length=40)),
                ('especie', models.CharField(max_length=20)),
                ('genero', models.CharField(max_length=1)),
                ('dia_creacion', models.DateTimeField(default=datetime.datetime(2022, 8, 28, 17, 54, 59, 852923, tzinfo=utc))),
            ],
        ),
    ]
