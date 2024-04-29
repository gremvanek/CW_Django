from django.urls import path

from spam_mailing.views import client_list, client_detail, client_create, client_update, client_delete, mailing_list, \
    mailing_detail, mailing_create, mailing_update, mailing_delete, message_list, message_detail, message_create, \
    message_update, message_delete, home_page

urlpatterns = [
    path('', home_page, name='home'),
    path("clients/", client_list, name="client_list"),
    path('client/<int:pk>/', client_detail, name='client_detail'),
    path('client/new/', client_create, name='client_create'),
    path('client/<int:pk>/edit/', client_update, name='client_update'),
    path('client/<int:pk>/delete/', client_delete, name='client_delete'),

    path('mailings/', mailing_list, name='mailing_list'),
    path('mailing/<int:pk>/', mailing_detail, name='mailing_detail'),
    path('mailing/new/', mailing_create, name='mailing_create'),
    path('mailing/<int:pk>/edit/', mailing_update, name='mailing_update'),
    path('mailing/<int:pk>/delete/', mailing_delete, name='mailing_delete'),

    path('messages/', message_list, name='message_list'),
    path('message/<int:pk>/', message_detail, name='message_detail'),
    path('message/new/', message_create, name='message_create'),
    path('message/<int:pk>/edit/', message_update, name='message_update'),
    path('message/<int:pk>/delete/', message_delete, name='message_delete'),
]
