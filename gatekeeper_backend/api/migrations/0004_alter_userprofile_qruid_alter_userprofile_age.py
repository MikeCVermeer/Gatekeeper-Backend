# Generated by Django 4.1.3 on 2022-11-25 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_userprofile_qruid_userprofile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='QrUid',
            field=models.PositiveIntegerField(default=0, max_length=8),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
    ]