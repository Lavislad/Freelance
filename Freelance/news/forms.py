from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text']

        widgets = {
            'title': TextInput(attrs={
                'id': 'title'
            }),
            'anons': TextInput(attrs={
                'id': 'anons'
            }),
            'full_text': Textarea(attrs={
                'id': 'full_text'
            })
        }