from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_class', 'batch', 'parent_mobile', 'is_active')
    list_filter = ('student_class', 'batch', 'is_active')
    search_fields = ('name', 'parent_mobile')
