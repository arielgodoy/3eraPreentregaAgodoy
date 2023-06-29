from . import views
from django.urls import path

urlpatterns = [    
    path('inicio/', views.inicio, name='inicio'),
    path('listarDocs/', views.listarDocs, name='listarDocs'),
    path('crea-Docs/', views.creaDocs, name='creaDocs'),
    path('update-Docs/<int:id>', views.updateDocs, name='updateDocs'),
    path('delete-Docs/<int:id>', views.deleteDocs, name='deleteDocs'),
    path('buscar-Docs/', views.buscarDocs, name='buscarDocs'),
]