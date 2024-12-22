from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def template_func(request):
    return render(request, 'second_task/template_func.html')


class TemplClass(TemplateView):
    template_name = 'second_task/template_class.html'
