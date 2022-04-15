from .models import devices
from django.db.models import F


class UserAgentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def stats(self, os_info):
        if "Windows" in os_info:
            devices.objects.all().update(windows=F('windows') + 1)
        elif "mac" in os_info:
            devices.objects.all().update(mac=F('mac') + 1)
        elif "iPhone" in os_info:
            devices.objects.all().update(iphone=F('iphone') + 1)
        elif "Android" in os_info:
            devices.objects.all().update(android=F('android') + 1)
        else:
            devices.objects.all().update(other=F('other') + 1)

    def __call__(self, request):

        # print(request.headers['User-Agent'])
        # print(request.META['HTTP_USER_AGENT'])

        self.stats(request.META['HTTP_USER_AGENT'])

        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        pass
