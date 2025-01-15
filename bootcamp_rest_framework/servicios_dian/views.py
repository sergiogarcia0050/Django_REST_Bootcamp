# from rest_framework .viewsets import ViewSet
# from rest_framework.response import Response

# from bootcamp_rest_framework.servicios_dian.models import ServiciosDian

# class serializadorDian(ViewSet):
#     class meta  :
#         model = ServiciosDian
#         fields = '__all__'



# class vistasDian(ViewSet):
#     queryset = ServiciosDian.objects.all()
#     serializer_class = serializadorDian




from zeep import Client, exceptions

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ExternalServiceView(APIView):
    def get(self, request):
            wsdl_url = "https://vpfe.dian.gov.co/WcfDianCustomerServices.svc?WSDL"  # Replace with the actual WSDL URL
            client = Client(wsdl_url)

            try:
                # Call the SOAP method with required parameters
                response = client.service.YourSoapMethodName(param1="value1", param2="value2")
                return Response({"response": response}, status=status.HTTP_200_OK)
            except exceptions.Error as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)