from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from quality_control.models import BugReport, FeatureRequest
from django.shortcuts import render, redirect
from .forms import BugReportForm, FeatureRequestForm
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

from django.views.generic import DetailView, UpdateView, DeleteView


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

def add_bug_report(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_report')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def add_feature_request_report(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_report')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})


def update_bug_report(request, bug_id):
    bugs = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bugs)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_detail', bug_id=bugs.id)
    else:
        form = BugReportForm(instance=bugs)
    return render(request, 'quality_control/bug_report_update.html', {'form': form, 'bug': bugs})

def feature_update_bug_report(request, feature_id):
    features = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=features)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', feature_id=features.id)
    else:
        form = FeatureRequestForm(instance=features)
    return render(request, 'quality_control/FeatureRequest_update.html', {'form': form, 'feature': features})

class BugUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_update.html'
    pk_url_kwarg = 'bug_id'
    def get_success_url(self):
        return reverse_lazy('quality_control:bug_detail', kwargs = {'bug_id': self.kwargs['bug_id']})

class FeatureUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/FeatureRequest_update.html'
    pk_url_kwarg = 'feature_id'

    def get_success_url(self):
        return reverse_lazy('quality_control:feature_detail', kwargs = {'feature_id': self.kwargs['feature_id']})

def delete_BugReport(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect('quality_control:bug_report')

def delete_FeatureRequest(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()
    return redirect('quality_control:feature_report')

class BugReportDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bug_list')
    template_name = 'quality_control/bug_report_delete.html'

    def get_success_url(self):
        return reverse_lazy('quality_control:bug_report')
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        return render(request, 'quality_control/bug_report_delete.html', {'bug': bug})
class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get_success_url(self):
        return reverse_lazy('quality_control:feature_report')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        return render(request, 'quality_control/FeatureRequest_delete.html', {'feature': feature})

# Create your views here.
