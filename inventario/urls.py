from django.urls import path
from . import views


urlpatterns = [

    path(
        'registrar/',
        views.registrar_movimiento,
        name='registrar_movimiento'
    ),

]