# Generated by Django 4.1.7 on 2023-03-17 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_common_words'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
    ]
