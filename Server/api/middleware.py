import sys
from datetime import datetime

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # İstek geldiğinde çalışır
        print(f"\n[{datetime.now()}] [MIDDLEWARE] New Request: {request.method} {request.path}")
        print(f"[{datetime.now()}] [MIDDLEWARE] Remote Addr: {request.META.get('REMOTE_ADDR')}")
        
        # Diğer middleware'lere geçiş
        response = self.get_response(request)
        
        # Yanıt dönerken çalışır
        print(f"[{datetime.now()}] [MIDDLEWARE] Response Status: {response.status_code}")
        return response
