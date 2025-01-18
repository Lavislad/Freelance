from .models import Feedback
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'user_name', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Title'
            }),
            'user_name': TextInput(attrs={
                'placeholder': 'User Name'
            }),
            'full_text': Textarea(attrs={
                'placeholder': 'Text'
            }),
            'date': DateTimeInput(attrs={
                'placeholder': 'Date',
                'type': 'datetime-local'
            }, format=('%Y-%m-%dT%H:%M'))
        }