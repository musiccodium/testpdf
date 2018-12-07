import base64
import logging

from django.http import HttpResponse
from django.template import loader
from django.template.loader import get_template
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from weasyprint import HTML

log = logging.getLogger('hero_track')


class PreviewSalaryTemplates(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        context = {}

        if True:
            html_template = get_template('salary_guarantee_template.html')
            html = html_template.render(context).encode(encoding="UTF-8")

            uri = request.build_absolute_uri()

            pdf_file = HTML(
                string=html,
                base_url=uri,
            ).write_pdf()

            response = HttpResponse(pdf_file, content_type='application/pdf')
            return response
        else:
            template = loader.get_template('salary_guarantee_template.html')
            response = template.render(context, request)

            return HttpResponse(response)
