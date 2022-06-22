from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    # path('json', views.json_response, name='json')
]
