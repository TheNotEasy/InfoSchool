# Generated by Django 4.1.7 on 2023-03-23 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='school',
        ),
    ]
