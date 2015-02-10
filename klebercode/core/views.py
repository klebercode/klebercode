# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from klebercode.context_processors import enterprise_proc

from klebercode.core.models import (Banner, Category, Content)
from klebercode.blog.models import Entry

from klebercode.core.forms import ContactForm


def home(request):
    context = {}
    context['blog_list'] = Entry.published.all()[:5]
    context['super_banner_list'] = Banner.published.filter(type=1)
    context['second_banner_list'] = Banner.published.filter(type=2)
    context['popup_banner_list'] = Banner.published.filter(type=3)[:1]

    return render(request, 'home.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


def contact(request):
    context = {}

    # contact
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_mail()
            context['contact_success'] = True
    else:
        form = ContactForm()

    context['contact_form'] = form

    return render(request, 'contact.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


def content(request, slug):
    context = {}

    category = Category.objects.filter(slug=slug)

    content_list = get_object_or_404(Content, category=category)
    # try:
    # except:
    #     content_list = ''

    context['content_list'] = content_list
    context['blog_list'] = Entry.published.filter(categories=category)[:6]

    return render(request, 'content.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))
