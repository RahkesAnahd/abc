from django.contrib import admin

from .models import students_data,students_marks

admin.site.register(students_data)
admin.site.register(students_marks)
