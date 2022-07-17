from django.core.mail import send_mail


def send_confirmation_mail(code, email):
    full_link = f'http://localhost:8000/api/v1/account/active/{code}'
    send_mail(
        'Activations code',
        full_link,
        'lgtahir93@gmail.com',
        [email]
    )