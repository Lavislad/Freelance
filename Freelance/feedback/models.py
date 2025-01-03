from django.db import models

class Feedback(models.Model):
    title = models.CharField('Title', max_length=100)
    user_name = models.CharField('User Name', max_length=30)
    full_text = models.TextField('Text')
    date = models.DateTimeField('Publication Date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фидбэк'
        verbose_name_plural = 'Фидбэк'