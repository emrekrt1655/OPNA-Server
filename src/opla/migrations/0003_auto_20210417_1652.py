# Generated by Django 3.1.5 on 2021-04-17 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opla', '0002_auto_20210417_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='level',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), (
                'B1', 'B1'), ('B2', 'B2'), ('C1', 'C1')], default='A1', max_length=2),
        ),
    ]