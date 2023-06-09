# Generated by Django 4.1.7 on 2023-03-24 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_remove_user_school_parentmeta_school_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='parent_meta',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.parentmeta'),
        ),
        migrations.AddField(
            model_name='user',
            name='student_meta',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.studentmeta'),
        ),
        migrations.AddField(
            model_name='user',
            name='teacher_meta',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.teachermeta'),
        ),
    ]
