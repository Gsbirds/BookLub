from django.contrib import admin
from .models import File, Common_words

# Register your models here.
class FileAdmin(admin.ModelAdmin):
    list_display=(
        "filepath",
        "id",
        "filename"
    )
admin.site.register(File, FileAdmin)

class Common_wordsAdmin(admin.ModelAdmin):
    list_display=(
        "file",
        "words",
        "number",
        "id"
    )
admin.site.register(Common_words, Common_wordsAdmin)

