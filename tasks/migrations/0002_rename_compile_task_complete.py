# Generated by Django 4.2.5 on 2023-09-09 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='compile',
            new_name='complete',
        ),
    ]
