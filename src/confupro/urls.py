from django.conf.urls import url

from django.views.generic import TemplateView


from confupro.views import (
	inicio,
	usuario_nuevo,
	usuario_login,
	usuario_logout,
	usuario_perfil,
	contacto,

	)

urlpatterns = [
    url(r'^$', inicio, name='inicio'),
    #url(r'^$', TemplateView.as_view(template_name='home.html'), name='inicio'),
    url(r'^usuario/nuevo/$', usuario_nuevo, name='usuario_nuevo'),
    url(r'^usuario/login/$', usuario_login, name='usuario_login'),
    url(r'^usuario/logout/$', usuario_logout, name='usuario_logout'),
    url(r'^usuario/perfil/$', usuario_perfil, name='usuario_perfil'),
    url(r'^contacto/$', contacto, name='contacto'),
]