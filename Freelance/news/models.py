from django.db import models

class Articles(models.Model):
    title = models.CharField('News Title', max_length=50)
    anons = models.CharField('News Anons', max_length=250)
    full_text = models.TextField('News Text')
    date = models.DateTimeField('Publication Date', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
