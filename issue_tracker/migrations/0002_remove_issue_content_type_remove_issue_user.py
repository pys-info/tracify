# Generated by Django 4.2.1 on 2023-05-23 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='user',
        ),
    ]
