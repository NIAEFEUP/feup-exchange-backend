from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class TestServiceView(APIView):
    """
    View that tests the connection to the FEUP Exchange service.
    """
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        """
        GET method of the test service view.
        """
        data = {
            'message': 'Yep, it\'s working!'
        }

        return Response(data=data, status=status.HTTP_200_OK)
