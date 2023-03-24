from django.contrib import admin
from .models import *


admin.site.register([School, User, ParentMeta, TeacherMeta, StudentMeta])