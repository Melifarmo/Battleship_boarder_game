from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import TemplateView, View, RedirectView


class IndexPageView(TemplateView):
    template_name = 'boarderGamesDjango/index.html'


def indexPage(request):
    return HttpResponse("Main page")