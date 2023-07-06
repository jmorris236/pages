from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class MathPageView(TemplateView):
    template_name = 'math.html'


class SciencePageView(TemplateView):
    template_name = 'science.html'


class CodingPageView(TemplateView):
    template_name = 'coding.html'
