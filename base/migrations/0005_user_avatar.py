# Generated by Django 5.0.3 on 2024-04-15 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_registeruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
    ]