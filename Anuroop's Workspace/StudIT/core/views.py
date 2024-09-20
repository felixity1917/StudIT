from django.shortcuts import render, redirect
from .forms import UserProfileForm, SubjectForm, StudySessionForm
from .models import UserProfile, StudySession

def user_profile_view(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form})

def create_study_session_view(request):
    if request.method == 'POST':
        form = StudySessionForm(request.POST)
        if form.is_valid():
            study_session = form.save(commit=False)
            study_session.creator = request.user
            study_session.save()
            return redirect('dashboard')
    else:
        form = StudySessionForm()

    return render(request, 'create_session.html', {'form': form})

def filter_study_sessions_view(request):
    subject = request.GET.get('subject')
    slot = request.GET.get('slot')

    filtered_sessions = StudySession.objects.all()

    if subject:
        filtered_sessions = filtered_sessions.filter(subject__name=subject)
    
    if slot:
        filtered_sessions = filtered_sessions.filter(subject__slots=slot)

    return render(request, 'study_sessions.html', {'sessions': filtered_sessions})

def home_view(request):
    return render(request, 'core/home.html') 