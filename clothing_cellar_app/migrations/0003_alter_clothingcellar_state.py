# Generated by Django 3.2.3 on 2021-05-28 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing_cellar_app', '0002_alter_clothingcellar_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothingcellar',
            name='state',
            field=models.CharField(choices=[['OK', 'PRODUCTO OK'], ['SOLD', 'VENDIDO'], ['DEFECTIVE', 'PRODUCTO DEFECTUOSO'], ['DAMAGED', 'PRODUCTO DAÑADO']], default='OK', max_length=20),
        ),
    ]
