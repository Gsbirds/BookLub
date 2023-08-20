from django.contrib import admin
from .models import File, CommonWords

# Register your models here.
class FileAdmin(admin.ModelAdmin):
    list_display=(
        "filepath",
        "id",
        "filename"
    )
admin.site.register(File, FileAdmin)

class CommonWordsAdmin(admin.ModelAdmin):
    list_display=(
        "pdf",
        "word",
    )
admin.site.register(CommonWords, CommonWordsAdmin)

