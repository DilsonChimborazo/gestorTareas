from django.urls import path
from .views import *

urlpatterns = [
    path('',listar,name='listar'),
    path('crear',crear,name='crear'),
    path('', tarea_Completa, name='tarea_completa'),
    path('', tarea_Incompleta, name='tarea_incompleta'),
]
