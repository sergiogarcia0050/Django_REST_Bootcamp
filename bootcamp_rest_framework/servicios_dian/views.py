from zeep import Client, exceptions
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from zeep.plugins import HistoryPlugin
from zeep.wsse.signature import Signature
import os

PRIVATE_KEY_PATH = os.getenv('PRIVATE_KEY_PATH')
CERTIFICATE_PATH = os.getenv('CERTIFICATE_PATH')




class ExternalServiceView(APIView):

    def post(self, request):
            wsdl_url = "https://vpfe.dian.gov.co/WcfDianCustomerServices.svc?WSDL"  # Replace with the actual WSDL URL
            client = Client(wsdl_url)
            data = request.data.get('NameMethotd', {})
            params = request.data.get('params', {})
            # session = requests.Session()
            # session.verify = True
            # session.cert = (CERTIFICATE_PATH, PRIVATE_KEY_PATH)  # Use PEM certificate & key

            # Initialize SOAP client with WSSE security and SSL authentication
            
            client = Client(wsdl_url, wsse=Signature(PRIVATE_KEY_PATH, CERTIFICATE_PATH))

            try:
                # Call the SOAP method with required parameters
                response = client.service[data](**params)
                
                return Response({"response": response}, status=status.HTTP_200_OK)
            except exceptions.Error as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)