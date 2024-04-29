from django.shortcuts import render, redirect

from spam_mailing.forms import ClientForm, MailingForm, MessageForm
from spam_mailing.models import Client, Mailing, Message


def home_page(request):
    return render(request, 'index.html')


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'spam_mail/client_list.html', {'clients': clients})


def client_detail(request, pk):
    client = Client.objects.get(pk=pk)
    return render(request, 'spam_mail/client_detail.html', {'client': client})


def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spam:client_list')
    else:
        form = ClientForm()
    return render(request, 'spam_mail/client_form.html', {'form': form})


def client_update(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('spam:client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'spam_mail/client_form.html', {'form': form})


def client_delete(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('spam:client_list')
    return render(request, 'spam_mail/client_delete.html', {'client': client})


def mailing_list(request):
    mailings = Mailing.objects.all()
    return render(request, 'spam_mail/mailing/mailing_list.html', {'mailings': mailings})


def mailing_detail(request, pk):
    mailing = Mailing.objects.get(pk=pk)
    return render(request, 'spam_mail/mailing/mailing_detail.html', {'mailing': mailing})


def mailing_create(request):
    if request.method == 'POST':
        form = MailingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spam:mailing_list')
    else:
        form = MailingForm()
    return render(request, 'spam_mail/mailing/mailing_form.html', {'form': form})


def mailing_update(request, pk):
    mailing = Mailing.objects.get(pk=pk)
    if request.method == 'POST':
        form = MailingForm(request.POST, instance=mailing)
        if form.is_valid():
            form.save()
            return redirect('spam:mailing_list')
    else:
        form = MailingForm(instance=mailing)
    return render(request, 'spam_mail/mailing/mailing_form.html', {'form': form})


def mailing_delete(request, pk):
    mailing = Mailing.objects.get(pk=pk)
    if request.method == 'POST':
        mailing.delete()
        return redirect('spam:mailing_list')
    return render(request, 'spam_mail/message/mailing_delete.html', {'mailing': mailing})


def message_list(request):
    messages = Message.objects.all()
    return render(request, 'spam_mail/message/message_list.html', {'messages': messages})


def message_detail(request, pk):
    message = Message.objects.get(pk=pk)
    return render(request, 'spam_mail/message/message_detail.html', {'message': message})


def message_create(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spam:message_list')
    else:
        form = MessageForm()
    return render(request, 'spam_mail/message/message_form.html', {'form': form})


def message_update(request, pk):
    message = Message.objects.get(pk=pk)
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('spam:message_list')
    else:
        form = MessageForm(instance=message)
    return render(request, 'spam_mail/message/message_form.html', {'form': form})


def message_delete(request, pk):
    message = Message.objects.get(pk=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('spam:message_list')
    return render(request, 'spam_mail/message/message_delete.html', {'message': message})
