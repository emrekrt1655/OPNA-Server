# Generated by Django 3.1.5 on 2021-04-15 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='subscription',
        ),
    ]
