from django import forms
from .models import Todo
# bu yapı serializers gibi
class TodoForm(forms.ModelForm):
    class Meta:
        model:Todo
        exclude=[]
        # çıkartmak istediğin fieldları yaz
