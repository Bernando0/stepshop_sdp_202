from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from authapp.models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = {'username', 'password'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = {'username', 'first_name', 'email', 'age', 'avatar', 'password'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']

        if data < 18:
            from django.forms import forms
            raise forms.ValidationError('Вы слишком молоды!')

        return data




class ShopUserRegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=128,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Логин',
                'id': 'login',
            }
        )
    )

    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'password1',
            }
        )
    )

    password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'password2',
            }
        )
    )

    email = forms.CharField(
        max_length=128,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Почта'
            }
        )
    )

    name1 = forms.CharField(
        max_length=128,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Имя'
            }
        )
    )

    age = forms.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'id': 'age',
                'placeholder': 'Возраст',
                'min' : 0,
                'max' : 100,
            }
        )
    )


    class Meta:
        model = ShopUser
        fields = {'username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']

        if data < 18:
            from django.forms import forms
            raise forms.ValidationError('Вы слишком молоды!')

        return data


