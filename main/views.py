from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact
from .service import send


# from .tasks import send_spam_email


class ContactView(CreateView):
    """Отображение формы подписи по email"""
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'main/contact.html'

    def form_valid(self, form):
        """Для передачи значения поля email в ф-ию 'send' - рассылки почты"""
        form.save()  # сохраняем форму
        # Передаём email пользователя в ф-ию send (отправляет письмо)
        send(form.instance.email)  # значение поля email
        return super().form_valid(form)
