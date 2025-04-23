from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Video, Comment, Like
from .forms import CustomUserCreationForm, VideoUploadForm, CommentForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video.save()
            return redirect('video_list')
    else:
        form = VideoUploadForm()
    return render(request, 'upload_video.html', {'form': form})

def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    comments = Comment.objects.filter(video=video)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.video = video
            comment.save()
            return redirect('video_detail', video_id=video.id)
    else:
        form = CommentForm()
    return render(request, 'video_detail.html', {'video': video, 'comments': comments, 'form': form})

@login_required
def like_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    Like.objects.get_or_create(user=request.user, video=video)
    return redirect('video_detail', video_id=video.id)

@login_required
def profile(request):
    videos = Video.objects.filter(author=request.user)
    return render(request, 'profile.html', {'videos': videos})