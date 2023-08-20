from django.db import models
from django.contrib.auth.models import User
import os.path


class File(models.Model):
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="", blank=True)
    author=models.ForeignKey(
        User,
        related_name="file",
        on_delete=models.CASCADE,
        null=True
    )
    words=models.TextField(blank=True)

    def filename(self):
        return os.path.basename(self.filepath.name)
    

class CommonWords(models.Model):
    pdf = models.ForeignKey(
        File,
        related_name="common_words",
        on_delete=models.CASCADE
    )
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.word