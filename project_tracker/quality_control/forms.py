from django import forms
from .models import BugReport, FeatureRequest
from django.forms import ModelForm

class BugReportForm(ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'description', 'status', 'priority', 'project', 'task']

class FeatureRequestForm(ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'status', 'priority', 'project', 'task']