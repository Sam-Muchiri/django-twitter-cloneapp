# Generated by Django 5.1 on 2024-10-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_remove_blogs_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='Avatar',
            field=models.ImageField(blank=True, default='default_pic.jpg', null=True, upload_to=''),
        ),
    ]
