# Generated by Django 3.2.3 on 2021-05-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing_cellar_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothingcellar',
            name='color',
            field=models.CharField(choices=[['#faf38c', 'AMARILLO'], ['#fc3b5a', 'ROJO'], ['#082c56', 'AZUL OSCURO'], ['#21637c', 'AZUL VERDOSO'], ['#ffffff', 'BLANCO'], ['#0b1518', 'NEGRO'], ['#7D7D7D', 'GRIS'], ['#7D7D7D', 'LILA'], ['#f3eea4', 'HUESO']], default='#7D7D7D', max_length=10),
        ),
    ]
