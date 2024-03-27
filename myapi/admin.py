from django.contrib import admin
from .models import *


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "language", "teacher", "students")


admin.site.register(Student),
admin.site.register(Teacher),
admin.site.register(Subject),
