from django.db import models
from account.models import User


class Feedback(models.Model):
    title = models.CharField('Title', max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author_name = models.CharField(default='default_author_name')
    full_text = models.TextField('Text')
    date = models.DateTimeField('Publication Date', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/feedback/{self.id}'

    class Meta:
        verbose_name = 'Фидбэк'
        verbose_name_plural = 'Фидбэки'