from __future__ import annotations

from django.contrib.auth.models import AbstractUser
from django.db import models


class CodeVerificationMixin:
    pass


class News(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Контент")


class School(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField("Название", max_length=50)
    email = models.EmailField("Электронная почта")
    number = models.CharField("Номер телефона", max_length=12)

    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True)

    schedule = models.JSONField(null=True)
    events = models.JSONField(null=True)


class StudentMeta(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField("Код", max_length=36)

    first_name = models.CharField("Имя", max_length=20)
    second_name = models.CharField("Фамилия", max_length=20)
    last_name = models.CharField("Отчество", max_length=20)

    grade = models.CharField("Класс", max_length=2)
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class TeacherMeta(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField("Код", max_length=36)

    first_name = models.CharField("Имя", max_length=20)
    second_name = models.CharField("Фамилия", max_length=20)
    last_name = models.CharField("Отчество", max_length=20)

    subjects = models.JSONField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class ParentMeta(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField("Код", max_length=36)

    first_name = models.CharField("Имя", max_length=20)
    second_name = models.CharField("Фамилия", max_length=20)
    last_name = models.CharField("Отчество", max_length=20)

    student = models.OneToOneField(StudentMeta, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class User(AbstractUser):
    code = models.CharField("Код", max_length=36)

    student_meta = models.OneToOneField(StudentMeta, on_delete=models.CASCADE, null=True)
    teacher_meta = models.OneToOneField(TeacherMeta, on_delete=models.CASCADE, null=True)
    parent_meta = models.OneToOneField(ParentMeta, on_delete=models.CASCADE, null=True)

    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
