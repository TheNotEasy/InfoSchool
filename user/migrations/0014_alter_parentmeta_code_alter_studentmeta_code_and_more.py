# Generated by Django 4.1.7 on 2023-03-24 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_school_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentmeta',
            name='code',
            field=models.CharField(max_length=36, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='studentmeta',
            name='code',
            field=models.CharField(max_length=36, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='teachermeta',
            name='code',
            field=models.CharField(max_length=36, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(max_length=36, verbose_name='Код'),
        ),
    ]
