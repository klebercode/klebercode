# coding: utf-8
from django import forms
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


class ContactForm(forms.Form):
    name = forms.CharField(label=u'Nome',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Nome'}))
    email = forms.EmailField(label=u'E-mail',
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control',
                                        'placeholder': 'E-mail'}))
    message = forms.CharField(label=u'Mensagem',
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control', 'rows': 6,
                                         'placeholder': 'Mensagem'}))

    def send_mail(self):
        subject = u'Contato do KleberCode (%s)' % self.cleaned_data['name']
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        message = render_to_string('contact_mail.txt', context)
        message_html = render_to_string('contact_mail.html', context)
        msg = EmailMultiAlternatives(subject, message,
                                     'no-reply@klebercode.com',
                                     ['klebess@gmail.com'])

        msg.attach_alternative(message_html, 'text/html')
        msg.send()
