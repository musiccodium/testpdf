from django.contrib import admin
from django.urls import path

from shironeko.views import PreviewSalaryTemplates, PdfTemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', PreviewSalaryTemplates.as_view(), name='salary-guarantee'),
    path('pdf/', PdfTemplate.as_view(), name='pdf-template'),
]
