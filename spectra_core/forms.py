from django import forms
from .models import Work

class WorkForm(forms.ModelForm):
    authors = forms.CharField(max_length=200)
    keywords = forms.CharField(max_length=200)

    class Meta:
        model = Work
        fields = ['title', 'abstract', 'publication_date', 'dmp', 'url', 'code_url', 'dataset_url', 'authors', 'keywords']