# Generated by Django 4.1.3 on 2022-11-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_userprofile_qruid_alter_userprofile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='QrUid',
            field=models.PositiveIntegerField(default=0),
        ),
    ]