from django.conf.urls.defaults import *


urlpatterns = patterns('pessoa.views',
    url(r'^$', 'manter', name='manter'),
    url(r'^(\d+)/sucesso/$', 'success', name='success'),
)