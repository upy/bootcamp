from django.utils.deprecation import MiddlewareMixin


class CustomMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print("request geldi")

    def process_response(self, request, response):
        print("response gitti")
        return response
