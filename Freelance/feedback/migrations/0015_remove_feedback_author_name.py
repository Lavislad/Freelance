# Generated by Django 5.1.4 on 2025-02-21 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0014_feedback_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='author_name',
        ),
    ]
