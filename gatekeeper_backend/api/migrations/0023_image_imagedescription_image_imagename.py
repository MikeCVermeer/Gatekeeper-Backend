# Generated by Django 4.1.3 on 2023-01-15 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_rename_image_image_image_image_imageowner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='ImageDescription',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='ImageName',
            field=models.CharField(default='Image', max_length=50),
        ),
    ]
