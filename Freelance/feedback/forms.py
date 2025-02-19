from .models import Feedback
from django.forms import ModelForm, TextInput, Textarea


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'full_text']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Title'
            }),
            'full_text': Textarea(attrs={
                'placeholder': 'Text'
            })
        }