from django.contrib import admin
from .models import Staff, StaffAttendance

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'mobile', 'is_active')
    list_filter = ('subject', 'is_active')

@admin.register(StaffAttendance)
class StaffAttendanceAdmin(admin.ModelAdmin):
    list_display = ('staff', 'date', 'status')
    list_filter = ('date', 'status')
