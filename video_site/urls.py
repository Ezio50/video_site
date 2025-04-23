from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from video_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.video_list, name='video_list'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='accounts_login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('upload/', views.upload_video, name='upload_video'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),
    path('video/<int:video_id>/like/', views.like_video, name='like_video'),
    path('profile/', views.profile, name='profile'),
    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)