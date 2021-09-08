from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='stream_list'),
    path('', views.streams, name='stream_list'), # todo: use generic view
    path('<int:pk>/', views.DetailView.as_view(), name='stream_detail'),
    path('<int:stream_id>/update/', views.update_stream, name='update_stream'),
    path('create/form', views.create_stream_form, name='create_stream_form'),
    path('create/', views.create_stream, name='create_stream'),
]