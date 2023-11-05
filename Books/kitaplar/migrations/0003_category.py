# Generated by Django 4.2.5 on 2023-11-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitaplar', '0002_library_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('slug', models.SlugField(default='', unique=True)),
            ],
        ),
    ]
