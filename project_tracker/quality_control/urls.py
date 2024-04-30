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
    path('features/new', views.add_feature_request_report, name='feature_bug_report'),

    path('bugs/<int:bug_id>/update/', views.update_bug_report, name='update_bug_report'),
    path('features/<int:feature_id>/update/', views.feature_update_bug_report, name='FeatureRequest_update'),
    path('bugs/<int:bug_id>/delete/', views.delete_BugReport, name='delete_BugReport'),
    path('features/<int:feature_id>/delete/', views.delete_FeatureRequest, name='delete_FeatureRequest'),



    # path('bugs/<int:bug_id>/update/', views.BugUpdateView.as_view(), name='update_bug_report'),
    # path('features/<int:feature_id>/update/', views.FeatureUpdateView.as_view(), name='FeatureRequest_update'),
    # path('bugs/<int:bug_id>/delete/', views.BugReportDeleteView.as_view(), name='delete_BugReport'),
    # path('features/<int:feature_id>/delete/', views.FeatureRequestDeleteView.as_view(), name='delete_FeatureRequest'),
]