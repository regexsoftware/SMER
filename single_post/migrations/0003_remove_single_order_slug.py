# Generated by Django 2.1.5 on 2019-10-20 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_post', '0002_auto_20191020_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='single_order',
            name='slug',
        ),
    ]