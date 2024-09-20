
from django.urls import path
from .views import user_profile_view, create_study_session_view, filter_study_sessions_view

urlpatterns = [
    path('profile/', user_profile_view, name='profile'),
    path('create-session/', create_study_session_view, name='create-session'),
    path('filter-sessions/', filter_study_sessions_view, name='filter-sessions'),
]
