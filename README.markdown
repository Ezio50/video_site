# VideoHub

VideoHub — это веб-приложение для загрузки, просмотра и управления видеоконтентом. Пользователи могут регистрироваться, входить в аккаунт, загружать видео, просматривать список видео, оставлять комментарии и ставить лайки. Приложение поддерживает мультиязычный интерфейс (русский и английский) и адаптивный дизайн.

## Основные функции

- Регистрация и авторизация пользователей.
- Загрузка и просмотр видео.
- Добавление комментариев и лайков к видео.
- Просмотр профиля с личными видео.
- Переключение языков (RU/EN).
- Адаптивный дизайн на основе Bootstrap 5.

## Технологии

- **Backend**: Python 3.12, Django 5.2
- **Database**: MySQL
- **Frontend**: HTML, CSS (Bootstrap 5), JavaScript
- **Localization**: Django i18n для поддержки русского и английского языков
- **Media**: Django для обработки видеофайлов

## Установка

### Требования

- Python 3.12
- MySQL
- GNU Gettext (для компиляции переводов на Windows)
- Виртуальное окружение (рекомендуется)

### Шаги установки

1. **Клонируйте репозиторий**:

   ```bash
   git clone <repository-url>
   cd videohub
   ```

2. **Создайте виртуальное окружение**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Установите зависимости**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте базу данных**:

   - Создайте базу данных в MySQL:

     ```sql
     CREATE DATABASE videohub;
     ```

   - Настройте параметры базы данных в `video_site/settings.py` или используйте `.env` файл:

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'videohub',
             'USER': 'your_username',
             'PASSWORD': 'your_password',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```

5. **Примените миграции**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Скомпилируйте переводы**:

   ```bash
   python manage.py compilemessages
   ```

7. **Создайте суперпользователя** (для доступа к админ-панели):

   ```bash
   python manage.py createsuperuser
   ```

8. **Запустите сервер**:

   ```bash
   python manage.py runserver
   ```

9. **Откройте приложение**:

   - Перейдите на `http://127.0.0.1:8000/`.
   - Админ-панель доступна по адресу `http://127.0.0.1:8000/admin/`.

## Структура проекта

```
videohub/
├── video_site/           # Основные настройки проекта
│   ├── settings.py       # Конфигурация Django
│   ├── urls.py           # Главные маршруты
│   └── ...
├── video_app/            # Приложение для функционала
│   ├── migrations/       # Миграции базы данных
│   ├── templates/        # HTML-шаблоны
│   │   ├── video_list.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── upload_video.html
│   │   ├── video_detail.html
│   │   └── profile.html
│   ├── locale/           # Файлы переводов (en, ru)
│   ├── models.py         # Модели данных (Video, Like, Comment)
│   ├── forms.py          # Формы (CustomUserCreationForm, VideoForm, CommentForm)
│   ├── views.py          # Представления
│   ├── urls.py           # Маршруты приложения
│   └── ...
├── media/                # Загруженные видеофайлы
├── requirements.txt      # Зависимости проекта
└── README.md             # Документация
```

## Использование

- **Главная страница** (`/`): Просмотр списка всех видео.
- **Регистрация** (`/register/`): Создание нового аккаунта.
- **Вход** (`/login/`): Авторизация.
- **Загрузка видео** (`/upload/`): Добавление нового видео (доступно авторизованным пользователям).
- **Профиль** (`/profile/`): Просмотр загруженных видео пользователя.
- **Детали видео** (`/video/<id>/`): Просмотр видео, комментариев и добавление лайков/комментариев.
- **Переключение языка**: Используйте выпадающее меню в навигационной панели.

## Разработка

- Для добавления новых функций создавайте ветки в Git:

  ```bash
  git checkout -b feature/new-feature
  ```

- После внесения изменений обновляйте переводы:

  ```bash
  python manage.py makemessages -l ru
  python manage.py makemessages -l en
  python manage.py compilemessages
  ```

## Будущие улучшения

- Хостинг приложения на сервере.
- Добавление функционала редактирования и удаления видео.
- Уведомления о новых комментариях и лайках.
- Улучшение дизайна (тёмная тема, анимации).
- Поиск и категоризация видео.