# Generated by Django 3.0.3 on 2020-04-24 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200424_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malurl',
            name='url',
            field=models.URLField(help_text='Please use the following format http://example.com or https://example.com', max_length=120),
        ),
    ]
