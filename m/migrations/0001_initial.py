# Generated by Django 3.0.4 on 2020-05-06 08:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiniUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('code', models.CharField(max_length=6, unique=True)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2020, 5, 6, 8, 52, 5, 13994, tzinfo=utc))),
                ('pseudo', models.CharField(max_length=30)),
                ('nb_access', models.IntegerField(default=0)),
            ],
        ),
    ]
