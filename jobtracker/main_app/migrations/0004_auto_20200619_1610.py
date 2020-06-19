# Generated by Django 3.0.7 on 2020-06-19 16:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_job_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='job',
            name='comment',
            field=models.TextField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 6, 19, 16, 10, 45, 758192, tzinfo=utc), verbose_name='Date applied'),
        ),
    ]
