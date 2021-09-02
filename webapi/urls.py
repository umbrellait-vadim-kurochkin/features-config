from django.urls import path
from . import views

urlpatterns = [
    path('streams/', views.stream_list),
]