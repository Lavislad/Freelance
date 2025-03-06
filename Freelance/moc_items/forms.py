from django.forms import DateTimeInput, ModelForm, Textarea, TextInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ["title", "anons", "full_text"]

        widgets = {
            "title": TextInput(attrs={"placeholder": "Title"}),
            "anons": TextInput(attrs={"placeholder": "Anons"}),
            "full_text": Textarea(attrs={"placeholder": "Text"}),
        }
