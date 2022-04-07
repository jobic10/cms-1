from django.http import Http404, request
from django.utils.deprecation import MiddlewareMixin


class FilterIpMiddleware(MiddlewareMixin):
    def process_request(self,request):
        allowed_ip=['192.168.1.1']
        ip=request.META.get('REMOTE_ADDR')
        print(ip)
        if ip not in allowed_ip:
            raise Http404
        return None