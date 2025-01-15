from rest_framework .views import APIView
from rest_framework.response import Response

class vistasDian(APIView):
    def get(self, request):
        return Response('Hello, World!')