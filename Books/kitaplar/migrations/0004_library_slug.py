# Generated by Django 4.2.5 on 2023-11-05 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitaplar', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]