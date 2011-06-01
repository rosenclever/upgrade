from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^upgrade/', include('upgrade.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include('admin.site.urls')),
    (r'^pessoa/', include('pessoa.urls', namespace='pessoa')),
    (r'^endereco/', include('endereco.urls', namespace='endereco')),
    (r'^telefone/', include('endereco.urls', namespace='telefone')),
	(r'^admin/(.*)', admin.site.root),
    url(r'^$', 'core.views.homepage', name='homepage'),
    
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': settings.MEDIA_ROOT }),
    )