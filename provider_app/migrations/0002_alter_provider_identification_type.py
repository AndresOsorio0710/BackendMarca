# Generated by Django 3.2 on 2021-05-17 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='identification_type',
            field=models.CharField(default='NOT', max_length=7),
        ),
    ]
