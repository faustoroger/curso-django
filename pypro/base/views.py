from django.http import HttpResponse


# from django.shortcuts import render


# Create your views here.

def home(request):
    raise ValueError()
    return HttpResponse('<html> \
                        <meta charset="UTF-8"> \
                        <body>Olá, Django!</body></html>',
                        content_type='text/html')
