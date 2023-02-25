from django.forms import ModelForm
from django import forms
from .models import Todo

# Create your models here.
class TodoForm(ModelForm):
    title = forms.CharField(label='Title', required=False)
    description = forms.CharField(label='Description', required=False, widget=forms.Textarea())
    class Meta:
        model = Todo
        fields = ['title', 'description']

class CheckboxForm(ModelForm):
    done = forms.CheckboxInput()
    class Meta:
        model = Todo
        fields = ['isDone']