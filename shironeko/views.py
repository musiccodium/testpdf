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

        filename = "/Users/pac/Documents/Code/testpdf/static/ductasia.jpg"
        with open(filename, "rb") as imagefile:
            encoded_string = base64.b64encode(imagefile.read())
            context["img"] = encoded_string
        #
        # html_template = get_template('salary_guarantee_template.html')
        # html = html_template.render(context).encode(encoding="UTF-8")
        # uri = request.build_absolute_uri()
        #
        # response = HttpResponse(content_type='application/pdf;')
        # response['Content-Disposition'] = 'inline; filename=salary_guarantee_form.pdf'
        #
        # HTML(
        #     string=html,
        #     base_url=uri,
        #     encoding="UTF-8"
        # ).write_pdf(response)
        #
        # return response

        template = loader.get_template('salary_guarantee_template.html')
        response = template.render(context, request)
        return HttpResponse(response)
