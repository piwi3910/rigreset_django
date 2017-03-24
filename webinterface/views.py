import django.shortcuts
from api.models import Miners, Heartbeat, Miner_status


def index(request):
    all_miners = Miners.objects.all()
    heartbeat = Heartbeat.objects.order_by('time')[0]

    context = {
        'all_miners': all_miners,
        'miner_status': Miner_status,
        'heartbeat': Heartbeat,
    }
    return django.shortcuts.render(request, 'webinterface/index.html', context)
