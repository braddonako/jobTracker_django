# Generated by Django 3.0.7 on 2020-06-17 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200617_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='comment',
            field=models.TextField(default='', max_length=250),
        ),
    ]