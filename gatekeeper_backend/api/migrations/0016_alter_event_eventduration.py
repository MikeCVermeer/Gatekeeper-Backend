# Generated by Django 4.1.3 on 2022-12-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_event_eventminimumage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='EventDuration',
            field=models.TimeField(),
        ),
    ]