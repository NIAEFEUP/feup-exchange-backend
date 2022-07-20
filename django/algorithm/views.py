from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import status

from .serializers import DeadlineSerializer

class DeadlineView(APIView):
    """
    View that fetches the datetime for when the algorithm is scheduled to execute
    """
    def get(self, request):
        """
        GET method of the dealine fetching view
        """
        serializer = DeadlineSerializer(data=request.data)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors)
