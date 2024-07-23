import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError
import json

class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.

        # TODO: handle strings that cannot be parsed/return errors
        address = request.query_params.get('address', '')

        try:
            parsed_components, address_type = self.parse(address)
        
            return Response({
                'input_string': address,
                'address_components': parsed_components,
                'address_type': address_type
            })
        except Exception as e:
            return Response({'error': 'could not parse'})

        

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        try:
            print(address)
            address_components = usaddress.tag(address)
            address_type = address_components[1]
            return address_components[0], address_type
        except usaddress.RepeatedLabelError as e:
            raise e