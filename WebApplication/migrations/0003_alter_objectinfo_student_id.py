# Generated by Django 3.2.7 on 2021-09-17 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApplication', '0002_auto_20210917_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectinfo',
            name='student_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]