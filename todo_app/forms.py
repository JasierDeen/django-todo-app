from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'memo': forms.Textarea(attrs={'class': 'form-control'}),
        #     'important': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        # }