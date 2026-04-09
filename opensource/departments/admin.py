from django.contrib import admin

# Register your models here.


from departments.models import Department


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('name',)
    list_per_page = 25



admin.site.register(Department, DepartmentAdmin)