from django.contrib import admin
from .models import Vacancy, Tags


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_tags')

    def display_tags(self, obj):
        return ", ".join([tag.title for tag in obj.tags.all()])

    display_tags.short_description = 'Теги'
