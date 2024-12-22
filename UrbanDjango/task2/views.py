from django.shortcuts import render


# Create your views here.
def template_func(request):
    return render(request, 'template_func.html')
