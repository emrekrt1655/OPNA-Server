# Generated by Django 3.1.5 on 2021-04-17 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opla', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='level',
            field=models.CharField(choices=[('AA', 'A1'), ('BB', 'A2'), (
                'B1', 'B1'), ('B2', 'B2'), ('C1', 'C1')], default='AA', max_length=2),
        ),
    ]
