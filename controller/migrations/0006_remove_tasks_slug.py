# Generated by Django 4.2.7 on 2023-11-11 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0005_alter_tasks_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='slug',
        ),
    ]
