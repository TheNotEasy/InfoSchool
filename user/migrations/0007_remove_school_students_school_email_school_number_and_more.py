# Generated by Django 4.1.7 on 2023-03-23 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_parentmeta_code_parentmeta_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='students',
        ),
        migrations.AddField(
            model_name='school',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='Электронная почта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='number',
            field=models.CharField(default='', max_length=12, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='users',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]