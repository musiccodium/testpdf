import logging

from django.http import HttpResponse
from django.template.loader import get_template
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from weasyprint import HTML

log = logging.getLogger('hero_track')


class PreviewSalaryTemplates(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        pdf = HTML("http://localhost:8000/pdf", base_url=request.build_absolute_uri()).write_pdf()
        return HttpResponse(pdf, content_type='application/pdf')


class PdfTemplate(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        html_template = get_template('salary_guarantee_template.html')
        html = html_template.render().encode(encoding="UTF-8")
        return HttpResponse(html)
