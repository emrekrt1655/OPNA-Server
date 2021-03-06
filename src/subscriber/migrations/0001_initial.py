# Generated by Django 3.1.5 on 2021-03-02 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscription', models.CharField(choices=[('english', 'English'), ('german', 'German'), ('turkish', 'Turkish'), ('french', 'French'), ('russian', 'Russian'), (
                    'ukranian', 'Ukrainian'), ('spanish', 'Spanish'), ('arabic', 'Arabic'), ('romanian', 'Romanian'), ('chinese', 'Chinese')], default='english', max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
