from core.models import *


def setting(request):
    context = {
        'settings' : Setting.objects.first()
    }
    return context