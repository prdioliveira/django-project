from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^listagem/$', views.pessoa_list, name='pessoa_listagem'),
    url(r'^cadastro/$', views.cad_pessoa, name='cadastro_pessoa'),
    url(r'^cadastro/(?P<pk>[0-9]+)/$', views.pessoa_detail, name='pessoa_detalhe'),
    url(r'^cadastro/(?P<pk>[0-9]+)/edit/$', views.pessoa_edit, name='pessoa_edit'),
]