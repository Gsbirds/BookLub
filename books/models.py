from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    name= models.CharField(max_length=500)
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="")
    author=models.ForeignKey(
        User,
        related_name="file",
        on_delete=models.CASCADE,
        null=True
    )
    def __str__(self):
        return str(self.name)