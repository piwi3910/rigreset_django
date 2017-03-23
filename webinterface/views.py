import django.shortcuts
from api.models import Miners, Heartbeat


def index(request):
    all_miners = Miners.objects.all()
    context = {
        'all_miners': all_miners,

                }
    return django.shortcuts.render(request, 'webinterface/index.html', context)
