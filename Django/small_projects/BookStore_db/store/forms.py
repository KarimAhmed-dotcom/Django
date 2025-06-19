from django import forms
from .models import Store


class BookForm(forms.ModelForm):
    class Meta :
        model=Store
        fields='__all__'
        
        widgets={
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enetr Name of The Book'
            }),
            'description':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Enetr Description'
            }),
            'rate':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Enetr Rate'
            }),
            'views':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Enetr Number Of Views'
            })
        }