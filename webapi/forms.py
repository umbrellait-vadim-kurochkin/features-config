from django import forms
from .models import Stream

class StreamForm(forms.ModelForm):
    title = forms.CharField(label='Название: ', max_length=200)
    code = forms.CharField(label='Код: ', min_length=3, max_length=30)
    description = forms.CharField(label='Описание: ', widget=forms.Textarea, required=False)

    class Meta:
        model = Stream
        fields = ['title', 'code', 'description']