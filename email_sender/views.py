from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class SendEmailView(APIView):
    def post(self, request, *args, **kwargs):
        subject = request.data.get('subject')
        message = request.data.get('message')
        recipient_list = request.data.get('recipient_list')
        from_email = 'leanmsan@gmail.com'  # Usando tu dirección de correo configurada

        if not subject or not message or not recipient_list:
            return Response({'error': 'Faltan datos'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            send_mail(subject, message, from_email, recipient_list)
            return Response({'success': 'Correo enviado'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
