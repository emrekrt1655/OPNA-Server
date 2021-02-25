# Generated by Django 3.1.5 on 2021-02-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headtitle', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('category', models.CharField(choices=[('english', 'English'), ('german', 'German'), ('turkish', 'Turkish'), ('french', 'French'), ('russian', 'Russian'), ('ukranian', 'Ukrainian'), ('spanish', 'Spanish'), ('arabic', 'Arabic'), ('romanian', 'Romanian'), ('chinese', 'Chinese')], default='english', max_length=50)),
                ('image', models.CharField(default='https://images.pexels.com/photos/97050/pexels-photo-97050.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940', max_length=1000)),
                ('excerpt', models.CharField(blank=True, max_length=300)),
                ('published', models.BooleanField(default=False)),
                ('day', models.CharField(max_length=2)),
                ('month', models.CharField(max_length=2)),
                ('year', models.CharField(max_length=4)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('newstitle_one', models.CharField(max_length=300)),
                ('news_one_content', models.TextField()),
                ('newstitle_two', models.CharField(max_length=300)),
                ('news_two_content', models.TextField()),
                ('newstitle_three', models.CharField(blank=True, max_length=300)),
                ('news_three_content', models.TextField(blank=True)),
                ('newstitle_four', models.CharField(blank=True, max_length=300)),
                ('news_four_content', models.TextField(blank=True)),
                ('newstitle_five', models.CharField(blank=True, max_length=300)),
                ('news_five_content', models.TextField(blank=True)),
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
