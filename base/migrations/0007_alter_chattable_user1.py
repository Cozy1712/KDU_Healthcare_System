# Generated by Django 5.0.3 on 2024-04-18 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_chattable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chattable',
            name='user1',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
