from django.contrib import admin
from .models import Fee

@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ('student', 'month', 'total_amount', 'paid_amount', 'status')
    list_filter = ('month',)
    search_fields = ('student__name',)
