# Generated by Django 5.1.4 on 2025-03-03 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='main/static/main/img/NoAvatarImage.svg', null=True, upload_to='users_avatars/', verbose_name='Аватар'),
        ),
    ]
