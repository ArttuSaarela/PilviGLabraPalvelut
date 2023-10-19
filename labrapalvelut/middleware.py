import datetime
import logging

class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        visitor_ip = request.META.get('REMOTE_ADDR')

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        log_entry = f'{timestamp} - IP: {visitor_ip} - Path: {request.path}\n'

        with open('logs.txt', 'a') as log_file:
            log_file.write(log_entry)

        response = self.get_response(request)
        return response
