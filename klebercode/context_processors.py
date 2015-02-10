# coding: utf-8
from django.shortcuts import get_object_or_404

from klebercode.core.models import Enterprise, Category, AREA_CHOICES, Social
from klebercode.blog.models import Entry


def enterprise_proc(request):
    """ View Function """
    try:
        enterprise = get_object_or_404(Enterprise, pk=1)
    except:
        enterprise = ''

    area_reverse = dict((v, k) for k, v in AREA_CHOICES)
    site = Category.objects.filter(area=area_reverse['Site'])
    menu = Category.objects.filter(area=area_reverse['Menu'])
    social = Social.objects.all()
    recent_posts = Entry.published.all()[:3]

    return {
        'enterprise': enterprise,
        'site': site,
        'menu': menu,
        'social': social,
        'recent_posts': recent_posts,
    }


class EnterpriseExtraContext(object):
    """ Class Based View """
    try:
        enterprise = get_object_or_404(Enterprise, pk=1)
    except:
        enterprise = ''

    area_reverse = dict((v, k) for k, v in AREA_CHOICES)
    site = Category.objects.filter(area=area_reverse['Site'])
    menu = Category.objects.filter(area=area_reverse['Menu'])
    social = Social.objects.all()
    recent_posts = Entry.published.all()[:3]

    extra_context = {
        'enterprise': enterprise,
        'site': site,
        'menu': menu,
        'social': social,
        'recent_posts': recent_posts,
        }

    def get_context_data(self, **kwargs):
        context = super(EnterpriseExtraContext,
                        self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context
