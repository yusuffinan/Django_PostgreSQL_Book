# Generated by Django 4.2.5 on 2023-11-05 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitaplar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='summary',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
