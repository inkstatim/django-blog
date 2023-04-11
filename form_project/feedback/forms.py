from django import forms
from .models import Feedback


# class FeedbackFrom(forms.Form):
#     fname = forms.CharField(max_length=30,min_length=2 ,label='Name', error_messages={
#         "max_length": "Слишком много символов, должно быть %(limit_value)d, сейчас символов %(show_value)d.",
#         "min_length": "Слишком мало символов, должно быть %(limit_value)d, сейчас символов  %(show_value)d.",
#         "required": "Обязательно к заполнению",})
#     lname = forms.CharField(max_length=30,min_length=2 ,label='Surname', error_messages={
#         "max_length": "Слишком много символов, должно быть %(limit_value)d, сейчас символов %(show_value)d.",
#         "min_length": "Слишком мало символов, должно быть %(limit_value)d, сейчас символов  %(show_value)d.",
#         "required": "Обязательно к заполнению",})
#     feedback = forms.CharField(widget=forms.Textarea(attrs={"rows": 2,"cols": 20}))
#     rating = forms.IntegerField(label='Рейтинг', max_value=10, min_value=1)
#

class FeedbackFrom(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        labels ={
            'name':'Имя',
            "surname":"Фамилия",
            "feedback":"Отзыв",
            "rating":"Рейтинг"
        }
