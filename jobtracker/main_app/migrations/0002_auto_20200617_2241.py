# Generated by Django 3.0.7 on 2020-06-17 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='cover_letter',
        ),
        migrations.AlterField(
            model_name='job',
            name='referral',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('update', models.CharField(choices=[('c', 'The job has been closed'), ('u', 'Update'), ('i', 'important')], default='c', max_length=2)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Job')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
