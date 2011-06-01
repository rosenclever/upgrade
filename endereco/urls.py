from django.conf.urls.defaults import *


urlpatterns = patterns('endereco.views',
    url(r'^$', 'manterEndereco', name='manterEndereco'),
    url(r'^(\d+)/sucesso/$', 'success', name='success'),
)