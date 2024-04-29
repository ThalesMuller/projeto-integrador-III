from django.urls import path, re_path

from . import views

urlpatterns = [
    path('create/', views.ComentarioCreateView.as_view(), name='Comentario_create'),
    # Retrieve Comentario list
    path('', views.ComentarioListView.as_view(), name='Comentario_list'),
    # Retrieve single Comentario object
    re_path(r'^(?P<pk>\d+)/$', views.ComentarioDetailView.as_view(), name='Comentario_detail'),
    # Update a Comentario
    re_path(r'^(?P<pk>\d+)/update/$', views.ComentarioUpdateView.as_view(), name='Comentario_update'),
    # Delete a Comentario
    re_path(r'^(?P<pk>\d+)/delete/$', views.ComentarioDeleteView.as_view(), name='Comentario_delete')
]
