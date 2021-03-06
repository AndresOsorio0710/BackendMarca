# Generated by Django 3.2 on 2021-05-17 03:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identification_type', models.CharField(default='NOT', max_length=5)),
                ('identification', models.CharField(default='NOT INCLUDED', max_length=15)),
                ('name', models.CharField(default='NOT INCLUDED', max_length=100)),
                ('address', models.CharField(default='NOT INCLUDED', max_length=80)),
                ('phone_number', models.CharField(default='NOT INCLUDED', max_length=12)),
                ('email', models.EmailField(default='notIncluded@marca.com', max_length=254)),
                ('description', models.TextField(default='NOT INCLUDED')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
