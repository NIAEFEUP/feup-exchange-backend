from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .send import send_mail_to_setudents


class EmailStudentView(APIView):
    """
    View that sends email to student alerting for allocation process.
    """
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        """
        Get method of email student view.
        """
         
        receivers = ['kikojpgoncalves@gmail.com']
        subject = "Tema"
        body = """Boa tarde a todos,

O processo de escolha de horarios...

Assim sendo...

Desejamos a todos um bom semestre, 
NIAEFEUP."""
        
        data = {
            'message': 'Success!',
            'body': body,
            'subject': subject,
        }
        
        try:
            send_mail_to_setudents(receivers, subject, body)
            
        except BaseException as be:
            print(be)
            return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        return Response(data=data, status=status.HTTP_200_OK)
