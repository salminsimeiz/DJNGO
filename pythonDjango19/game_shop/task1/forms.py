from django import forms


class ContactForm(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(min_length=8, label='Введите пароль', widget=forms.PasswordInput)
    repeat_password = forms.CharField(min_length=8, label='Повторите пароль', widget=forms.PasswordInput)
    age = forms.IntegerField(min_value=12, max_value=140, label='Введите свой возраст')
