# Generated by Django 4.2.5 on 2023-11-06 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitaplar', '0006_library_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authorr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=50)),
                ('slug', models.SlugField(default='', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisherr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('slug', models.SlugField(default='', unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='library',
            name='author',
        ),
        migrations.RemoveField(
            model_name='library',
            name='publisher',
        ),
        migrations.AddField(
            model_name='library',
            name='author',
            field=models.ManyToManyField(to='kitaplar.authorr'),
        ),
        migrations.AddField(
            model_name='library',
            name='publisher',
            field=models.ManyToManyField(to='kitaplar.publisherr'),
        ),
    ]
