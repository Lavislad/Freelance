from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Title'
            }),
            'anons': TextInput(attrs={
                'placeholder': 'Anons'
            }),
            'full_text': Textarea(attrs={
                'placeholder': 'Text'
            }),
            'date': DateTimeInput(attrs={
                'placeholder': 'Date',
                'type': 'datetime-local'
            }, format=('%Y-%m-%dT%H:%M'))
        }