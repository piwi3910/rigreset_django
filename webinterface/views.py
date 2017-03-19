import django.shortcuts


def index(request):
    context = {}
    return django.shortcuts.render(request, 'webinterface/index.html', context)
