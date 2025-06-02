from django.db import models
from account.models import User


class Tags(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    payment = models.CharField()
    description = models.TextField(max_length=1500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tags, related_name='vacancies', verbose_name='Теги')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

