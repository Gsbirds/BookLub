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
    def filename(self):
        return os.path.basename(self.filepath.name)
    
class Common_words(models.Model):
    file=models.ForeignKey(
        File,
        related_name="file",
        on_delete=models.CASCADE,
        null=True
    )
    words=models.CharField(max_length=500)
    number= models.CharField(max_length=2)
