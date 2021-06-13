from django import forms
from Main.models import Author, Quote

######################################################################################################################


class FormAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'name',
        ]
        labels = {
            'name': 'Автор цитаты',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Укажите автора цитаты',
                }
            )
        }


######################################################################################################################


class FormQuote(forms.ModelForm):
    class Meta:
        model = Quote
        fields = [
            'quote',
        ]
        labels = {
            'quote': 'Текст цитаты',
        }
        widgets = {
            'quote': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Напишите текст цитаты',
                }
            ),
        }


######################################################################################################################
