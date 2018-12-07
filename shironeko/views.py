import logging, datetime, pytz, locale

from rest_framework import viewsets
from num2words import num2words
from rest_framework.decorators import list_route
from rest_framework.pagination import PageNumberPagination
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from weasyprint import HTML

from django.template.loader import render_to_string

log = logging.getLogger('hero_track')

class PreviewSalaryTemplates(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        html_string = render_to_string(template_name='salary_guarantee_template.html')
        response = HttpResponse(content_type='application/pdf;')
        response['Content-Disposition'] = 'inline; filename=salary_guarantee_form.pdf'
        HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf(response)
        print(response)
        return response