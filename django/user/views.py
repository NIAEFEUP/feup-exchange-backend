from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import AdminRegistrationSerializer

class AdminView(APIView):
    """
    View that implements various operations involving platform administrators.
    """
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        """
        Allows to register a new platform administrator in the system.
        """
        serializer = AdminRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            admin = serializer.save()
            return Response(data={
                "response": "Succesfully registered a new admin",
                "email": admin.email
            }, status=status.HTTP_200_OK)

        return Response(data=serializer.errors)

class AdminTestServiceView(APIView):
    """
    View that tests the connection to the FEUP Exchange service.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get(self, request):
        """
        GET method of the admin test service view.
        """
        data = {
            'message': 'Yep, it\'s working (but only for admins)!'
        }

        return Response(data=data, status=status.HTTP_200_OK)