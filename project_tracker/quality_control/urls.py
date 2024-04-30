from django.urls import path
from . import views

app_name = 'quality_control'  # Определение пространства имён

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_report'),
    path('features/', views.feature_list, name='feature_report'),
    path('bugs/<int:bug_id>/', views.ClassBugDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.ClassFeatureDetailView.as_view(), name='feature_detail'),
    path('bugs/new', views.add_bug_report, name='add_bug_report'),
    path('features/new', views.add_feature_request_report, name='feature_bug_report')
]