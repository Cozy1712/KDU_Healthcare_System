# Generated by Django 5.0.3 on 2024-04-15 22:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user2', models.CharField(max_length=200, null=True)),
                ('chat', models.CharField(max_length=200, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
