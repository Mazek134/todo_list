from django.contrib import admin

# Register your models here.
from .models import Task


# udekorowana klasa admina dla modelu task - dostosowanie panelu admina w danym modelu
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ('task_desc', 'status', 'create_date')
    date_hierarchy = 'create_date'
