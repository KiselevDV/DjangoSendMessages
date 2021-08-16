from django.core.mail import send_mail


def send(user_email):
    """Стандартная рассылка почты в Django"""
    send_mail(
        'Вы подписались на рассылку',
        'Мы будем присылать вам много спама',
        'djangosc876@gmail.com',  # отправитель
        [user_email],  # получатель
        fail_silently=False,
    )
