# Generated by Django 3.1.5 on 2021-04-16 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opba', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bible',
            name='chapter',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
