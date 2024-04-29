from django.http import HttpResponse
from django.urls import reverse
def index(request):
    bug_report_url = reverse('quality_control:bug_report')

    feature_report_url = reverse('quality_control:feature_report')

    html = f"<h1>Система контроля качества</h1>"
    html += f"<a href='{bug_report_url}'>Список всех багов</a><br>"
    html += f"<a href='{feature_report_url}'>Запросы на улучшение</a>"

    return HttpResponse(html)
def bug_list(request):
    html = f'<h1> Список отчетов об ошибках </h1>'
    return HttpResponse(html)

def feature_list(request):
    html = f'<h1> Список запросов на улучшение </h1>'
    return HttpResponse(html)

def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")

def feature_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")

# Create your views here.
