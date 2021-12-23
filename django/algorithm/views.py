from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class AlgorithmScheduleView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        data = {
            'message': 'Scheduled the algorithm!'
        }

        return Response(data=data, status=status.HTTP_200_OK)
