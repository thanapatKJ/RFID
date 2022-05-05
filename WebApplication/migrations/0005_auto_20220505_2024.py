# Generated by Django 3.2.7 on 2022-05-05 20:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApplication', '0004_auto_20211209_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notfound',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApplication.objectinfo'),
        ),
        migrations.AlterField(
            model_name='notfound',
            name='takeout_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 20, 24, 22, 417560)),
        ),
    ]