from django.http import HttpResponse
from django.views.generic.base import View, TemplateView
from django.template import RequestContext

import datetime


class Home(TemplateView):
    template_name = 'frontend/index.html'

    def init(self, request, kwargs):
        return {
            'time': datetime.datetime.now(),
        }

    def get(self, request, **kwargs):
        return self.render_to_response(
            self.init(request, kwargs),
        )
