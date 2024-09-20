from django import forms
from .models import UserProfile, Subject, StudySession

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['branch', 'hostel_block', 'subjects']
        widgets = {
            'subjects': forms.CheckboxSelectMultiple(),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'slots']

class StudySessionForm(forms.ModelForm):
    class Meta:
        model = StudySession
        fields = ['subject', 'date', 'start_time', 'location', 'platform']
