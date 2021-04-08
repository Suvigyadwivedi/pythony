from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Lets rule the world.")