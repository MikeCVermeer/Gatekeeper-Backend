# Generated by Django 4.1.3 on 2023-01-23 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_alter_userprofile_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
    ]
