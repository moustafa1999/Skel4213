# Generated by Django 2.2.24 on 2022-02-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_sensor_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='time',
            field=models.CharField(max_length=60),
        ),
    ]
