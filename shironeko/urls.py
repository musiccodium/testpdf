from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from shironeko.views import PreviewSalaryTemplates

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', PreviewSalaryTemplates.as_view(), name='salary-guarantee'),
]
