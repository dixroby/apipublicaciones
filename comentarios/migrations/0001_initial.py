# Generated by Django 2.2.14 on 2020-12-04 05:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2020, 12, 3, 23, 25, 54, 778108))),
            ],
        ),
    ]