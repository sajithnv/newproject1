# Generated by Django 2.1 on 2021-03-11 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=100, verbose_name='the title'),
        ),
    ]
