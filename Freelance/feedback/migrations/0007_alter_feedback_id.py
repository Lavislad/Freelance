# Generated by Django 5.1.4 on 2025-02-17 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0006_alter_feedback_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
