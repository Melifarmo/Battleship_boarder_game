from django.shortcuts import render
from django.views.generic.base import TemplateView, View, RedirectView


class IndexPageView(TemplateView):
    template_name = 'battleShipsApp/index.html'
