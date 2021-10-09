from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('clientes/',views.clientes),
    path('<int:cliente_id>/',views.clientes_datail),
]
