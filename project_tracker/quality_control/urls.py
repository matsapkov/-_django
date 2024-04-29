from django.urls import path
from . import views

app_name = 'quality_control'  # Определение пространства имён

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_report'),
    path('features/', views.feature_list, name='feature_report'),
    path('bug/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('feature/<int:feature_id>/', views.feature_detail, name='feature_detail'),
]