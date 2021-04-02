from django import forms
from Main.models import Quote

######################################################################################################################


class FormCreateQuote(forms.ModelForm):
    class Meta:
        model = Quote
        fields = [
            'author',
            'quote',
        ]
        labels = {
            'author': 'Автор цитаты',
            'quote': 'Текст цитаты',
        }
        widgets = {
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите автора цитаты',
                }
            ),
            'quote': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
        help_texts = {
            'author': 'Обязательное поле. Только английские буквы.',
            'quote': 'Пароль не должен совпадать с логином и состоять только из цифр.',
        }


######################################################################################################################
