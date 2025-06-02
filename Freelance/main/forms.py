from .models import Vacancy
from django.forms import ModelForm, TextInput, Textarea, CheckboxSelectMultiple


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'payment', 'description', 'tags']

        widgets = {
            'title': TextInput(attrs={
                'id': 'title'
            }),
            'payment': TextInput(attrs={
                'id': 'payment'
            }),
            'description': Textarea(attrs={
                'id': 'text'
            })
        }