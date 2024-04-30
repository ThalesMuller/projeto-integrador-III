from django.urls import path, re_path

from . import views

urlpatterns = [
    path('create/', views.UsuarioCreateView.as_view(), name='Usuario_create'),
    # Retrieve Usuario list
    path('', views.UsuarioListView.as_view(), name='Usuario_list'),
    # Retrieve single Usuario object
    re_path(r'^(?P<pk>\d+)/$', views.UsuarioDetailView.as_view(), name='Usuario_detail'),
    # Update a Usuario
    re_path(r'^(?P<pk>\d+)/update/$', views.UsuarioUpdateView.as_view(), name='Usuario_update'),
    # Delete a Usuario
    re_path(r'^(?P<pk>\d+)/delete/$', views.UsuarioDeleteView.as_view(), name='Usuario_delete')
]
