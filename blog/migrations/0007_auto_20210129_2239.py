# Generated by Django 3.1.4 on 2021-01-30 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210129_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='No-Slug', max_length=200, unique=True),
        ),
    ]
