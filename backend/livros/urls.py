from django.urls import path, re_path

from . import views

urlpatterns = [
    path('create/', views.LivroCreateView.as_view(), name='Livro_create'),
    # Retrieve Livro list
    path('', views.LivroListView.as_view(), name='Livro_list'),
    # Retrieve single Livro object
    re_path(r'^(?P<pk>\d+)/$', views.LivroDetailView.as_view(), name='Livro_detail'),
    # Update a Livro
    re_path(r'^(?P<pk>\d+)/update/$', views.LivroUpdateView.as_view(), name='Livro_update'),
    # Delete a Livro
    re_path(r'^(?P<pk>\d+)/delete/$', views.LivroDeleteView.as_view(), name='Livro_delete')
    ]
