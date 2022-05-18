from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class AdminTestServiceView(APIView):
    """
    View that tests the connection to the FEUP Exchange service.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get(self, request):
        """
        GET method of the test service view.
        """
        data = {
            'message': 'Yep, it\'s working (but only for admins)!'
        }

        return Response(data=data, status=status.HTTP_200_OK)