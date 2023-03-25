from django import forms
from .models import Todo
# bu yapı serializers gibi
class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        # fields="__all__"
        exclude=[]
        # çıkartmak istediğin fieldları yaz
        
