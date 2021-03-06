# Generated by Django 3.1.5 on 2021-04-15 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bible',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('headtitle', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image', models.CharField(
                    default='https://images.pexels.com/photos/1682559/pexels-photo-1682559.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260', max_length=1000)),
                ('excerpt', models.CharField(blank=True, max_length=300)),
                ('published', models.BooleanField(default=False)),
                ('day', models.CharField(max_length=2)),
                ('month', models.CharField(max_length=2)),
                ('year', models.CharField(max_length=4)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('chapter', models.CharField(max_length=300)),
                ('chapter_content', models.TextField()),
                ('vocab_one', models.CharField(max_length=200)),
                ('vocab_one_mean', models.TextField()),
                ('vocab_two', models.CharField(max_length=200)),
                ('vocab_two_mean', models.TextField()),
                ('vocab_three', models.CharField(max_length=200)),
                ('vocab_three_mean', models.TextField()),
                ('vocab_four', models.CharField(blank=True, max_length=200)),
                ('vocab_four_mean', models.TextField(blank=True)),
                ('vocab_five', models.CharField(blank=True, max_length=200)),
                ('vocab_five_mean', models.TextField(blank=True)),
            ],
        ),
    ]
