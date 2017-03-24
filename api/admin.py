from django.contrib import admin
from .models import Miners, Heartbeat, test

admin.site.register(Miners)
admin.site.register(Heartbeat)
admin.site.register(test)

