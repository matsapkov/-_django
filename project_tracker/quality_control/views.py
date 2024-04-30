# from django.http import HttpResponse
# from django.urls import reverse
# from quality_control.models import BugReport, FeatureRequest
# def index(request):
#     bug_report_url = reverse('quality_control:bug_report')
#
#     feature_report_url = reverse('quality_control:feature_report')
#
#     html = f"<h1>Система контроля качества</h1>"
#     html += f"<a href='{bug_report_url}'>Список всех багов</a><br>"
#     html += f"<a href='{feature_report_url}'>Запросы на улучшение</a>"
#
#     return HttpResponse(html)
#
# from django.views import View
# class indexView(View):
#     def index(self):
#         bug_report_url = reverse('quality_control:bug_report')
#         feature_report_url = reverse('quality_control:feature_report')
#         html = f"<h1>Система контроля качества</h1>"
#         html += f"<a href='{bug_report_url}'>Список всех багов</a><br>"
#         html += f"<a href='{feature_report_url}'>Запросы на улучшение</a>"
#
#         return HttpResponse(html)
#
# def bug_list(request):
#     bugs = BugReport.objects.all()
#     html = f'<h1> Список отчетов об ошибках </h1>'
#     for bug in bugs:
#         html += f'<li><a href="{bug.id}/"> <br>Title: {bug.title}<br> Status: {bug.status}</a></li>'
#         html += '</ul>'
#     return HttpResponse(html)
#
# from django.views.generic import DetailView
# class ClassBugDetailView(DetailView):
#     model = BugReport
#     pk_url_kwarg = 'bug_id'
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         bug = self.object
#         html = f'<h1>{bug.title}</h1><p>{bug.description}</p><p>Status: {bug.status}</p><p>Priority level: {bug.priority}</p><p>Project: {bug.project}</p><p>Linked task: {bug.task}</p>'
#         return HttpResponse(html)
#
# def feature_list(request):
#     features = FeatureRequest.objects.all()
#     html = f'<h1> Список запросов на улучшение </h1>'
#     for feature in features:
#         html += f'<li><a href="{feature.id}/"><br>Title: {feature.title}<br>Status: {feature.status}</a></li>'
#     html += '</ul>'
#     return HttpResponse(html)
#
# class ClassFeatureDetailView(DetailView):
#     model = FeatureRequest
#     pk_url_kwarg = 'feature_id'
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         feature = self.object
#         html = f'<h1>{feature.title}</h1><p>{feature.description}</p><p>Status: {feature.status}</p><p>Priority level: {feature.priority}</p><p>Project: {feature.project}</p><p>Linked task: {feature.task}</p>'
#         return HttpResponse(html)


from django.shortcuts import render, get_object_or_404
from quality_control.models import BugReport, FeatureRequest

def index(request):
    return render(request, 'quality_control/index.html')

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_report.html', {'bug_report': bugs})
def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_report.html', {'feature_report': features})

def bug_detail(request, bug_id):
    bug = BugReport.objects.get(id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})

def feature_detail(request, feature_id):
    feature = FeatureRequest.objects.get(id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})

from django.views.generic import DetailView
class ClassBugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        return render(request, 'quality_control/bug_detail.html', {'bug': bug})
class ClassFeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        return render(request, 'quality_control/feature_detail.html', {'feature': feature})


# def bug_detail(request, project_id):
#     project = get_object_or_404(Project, id=project_id)
#     return render(request, 'tasks/project_detail.html', {'project': project})
#
# def feature_detail(request, project_id, task_id):
#     task = get_object_or_404(Task, id=task_id, project_id=project_id)
#     return render(request, 'tasks/task_detail.html', {'task': task})
#

# Create your views here.
