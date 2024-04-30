from django.urls import path, re_path

from . import views

urlpatterns = [
    path('create/', views.ResenhaCreateView.as_view(), name='Resenha_create'),
    # Retrieve Resenha list
    path('', views.ResenhaListView.as_view(), name='Resenha_list'),
    # Retrieve single Resenha object
    re_path(r'^(?P<pk>\d+)/$', views.ResenhaDetailView.as_view(), name='Resenha_detail'),
    # Update a Resenha
    re_path(r'^(?P<pk>\d+)/update/$', views.ResenhaUpdateView.as_view(), name='Resenha_update'),
    # Delete a Resenha
    re_path(r'^(?P<pk>\d+)/delete/$', views.ResenhaDeleteView.as_view(), name='Resenha_delete')
]
