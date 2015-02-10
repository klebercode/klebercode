from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from filebrowser.sites import site

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', 'klebercode.core.views.home', name='home'),

    url(r'^contato/$', 'klebercode.core.views.contact', name='contact'),

    url(r'^site/(?P<slug>[-\w]+)/$', 'klebercode.core.views.content',
        name='site'),
    url(r'^inicio/(?P<slug>[-\w]+)/$', 'klebercode.core.views.content',
        name='menu'),

    url(r'^blog/', include('klebercode.blog.urls', namespace='blog',
        app_name='blog')),

    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),

    # tinymce
    url(r'^tinymce/', include('tinymce.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# )
