# Generated by Django 3.0.7 on 2020-06-17 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200617_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='cover_letter',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='job',
            name='followup',
            field=models.TextField(max_length=1000),
        ),
    ]
