from django.contrib import admin
from .models import File

# Register your models here.
class FileAdmin(admin.ModelAdmin):
    list_display=(
        "name",
        "filepath",
        "id"
    )
admin.site.register(File, FileAdmin)
