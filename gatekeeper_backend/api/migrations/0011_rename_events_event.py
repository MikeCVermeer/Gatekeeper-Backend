# Generated by Django 4.1.3 on 2022-12-20 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_events'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
    ]
