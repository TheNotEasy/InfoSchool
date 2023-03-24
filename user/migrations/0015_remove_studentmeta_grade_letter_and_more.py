# Generated by Django 4.1.7 on 2023-03-24 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_parentmeta_code_alter_studentmeta_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmeta',
            name='grade_letter',
        ),
        migrations.RemoveField(
            model_name='studentmeta',
            name='grade_num',
        ),
        migrations.AddField(
            model_name='studentmeta',
            name='grade',
            field=models.CharField(default='1', max_length=2, verbose_name='Класс'),
            preserve_default=False,
        ),
    ]