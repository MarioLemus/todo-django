# Generated by Django 4.1.7 on 2023-02-24 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='complitionDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(null=True),
        ),
    ]