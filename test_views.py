from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView


def test_error_notifier(request):

    # Raise an exception to generate an error
    raise Exception("This is a test error")


class TemplateViewTest(TemplateView):
    template_name = "test.html"

    def post(self, request):
        a = 1/0
        return HttpResponse("test")


class APITest(APIView):

    def get(self, request, pk):
        a = 1/0
        return Response({"test": "test"})

    def post(self, request, pk):
        a = 1/0
        return Response({"test": "test"})

    def put(self, request, pk):
        a = 1/0
        return Response({"test": "test"})
