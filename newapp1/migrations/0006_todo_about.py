# Generated by Django 2.1 on 2021-03-12 14:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newapp1', '0005_auto_20210312_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='about',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='About_Title '),
            preserve_default=False,
        ),
    ]