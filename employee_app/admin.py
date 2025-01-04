from django.contrib import admin
from .models import Position, Employee


class PositionAdmin(admin.ModelAdmin):
    list_display = ('title')
    search_fields = ('title')

admin.site.register(Position, PositionAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'emp_code', 'mobile', 'position')
    search_fields = ('full_name', 'emp_code', 'mobile', 'position')

admin.site.register(Employee, EmployeeAdmin)