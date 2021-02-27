from django.core.mail import send_mail
from django.conf import settings

def send_mail_to_setudents(student_email, subject, body):    
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        student_email,
        fail_silently=False,
    )