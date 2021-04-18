from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .schemas import TestServiceSuccessResponse

class TestServiceView(APIView):
    """
    View that tests the connection to the FEUP Exchange service.
    """
    permission_classes = []
    authentication_classes = []

    @swagger_auto_schema(
        operation_id="Test Service",
        operation_description="Endpoint to test the availability of the FEUP Exchange service.",
        responses={
            200: TestServiceSuccessResponse,
        }
    )
    def get(self, request):
        """
        GET method of the test service view.
        """
        data = {
            'message': 'Yep, it\'s working!'
        }

        return Response(data=data, status=status.HTTP_200_OK)
