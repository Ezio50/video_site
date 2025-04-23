from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Video, Comment

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': 'Имя пользователя',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }
        help_texts = {
            'username': 'Обязательно. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_',
            'password1': 'Пароль должен содержать минимум 8 символов, не быть слишком простым, не совпадать с личной информацией и не состоять только из цифр.',
            'password2': 'Введите пароль еще раз для подтверждения.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = self.Meta.help_texts['password1']
        self.fields['password2'].help_text = self.Meta.help_texts['password2']

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'video_file': 'Файл видео',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': 'Комментарий',
        }