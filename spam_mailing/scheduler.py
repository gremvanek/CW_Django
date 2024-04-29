from datetime import datetime, timedelta
from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail

from spam_mailing.models import Mailing, MailingLog


def run_mailing():
    # Запуск рассылки
    print('Запуск рассылки')

    # Получаем текущее время
    current_time = datetime.now().time()
    current_date = datetime.now().date()
    mailing = Mailing.objects.all()

    # Получаем все рассылки
    print('Получаем все рассылки')
    print(mailing)

    for el in mailing:
        email_list = el.client.values_list('email', flat=True)

        # Отправляем сообщения рассылки
        print('Отправляем сообщения рассылки')
        print(email_list)

        if (el.send_time.time() <= current_time and
                el.send_time.date() == current_date and el.status == 'started'):
            try:
                send_mail(
                    subject=el.message_set.first().subject,
                    message=el.message_set.first().body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=email_list,
                )

                if el.frequency == 'daily':
                    el.send_time += timedelta(days=1)
                elif el.frequency == 'weekly':
                    el.send_time += timedelta(weeks=1)
                elif el.frequency == 'monthly':
                    el.send_time += timedelta(days=30)
                el.save()

                # Обновляем время следующей отправки и статус рассылки
                print('Обновляем время следующей отправки и статус рассылки')
                MailingLog.objects.create(mailing=el, status='Sent', server_response='Complete')
            except SMTPException as e:
                # Ошибка отправки
                print('Ошибка отправки')
                MailingLog.objects.create(mailing=el, status='Fail',
                                          server_response=f"Не удалось отправить сообщение: {str(e)}")
            except Exception as e:
                # Неожиданная ошибка
                print('Неожиданная ошибка')
                MailingLog.objects.create(mailing=el, status='Fail',
                                          server_response=f"Произошла неожиданная ошибка: {str(e)}")
