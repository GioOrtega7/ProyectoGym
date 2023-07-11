from django.contrib import admin
from django.urls import path
from principal.views import *


urlpatterns = [
    
    ##cargo

   path('cargo/', ListadoCargo.as_view(template_name = "crud/cargo/tables.html"), name='leercargo'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cargo registro 
   path('cargo/detalle/<int:pk>', CargoDetalle.as_view(template_name = "crud/cargo/detalle.html"), name='detallecargo'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cargo o registro  
   #path('cargo/crear', CargoCrear.as_view(template_name = "crud/cargo/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cargo registro de la Base de Datos 
   path('cargo/editar/<int:pk>', CargoActualizar.as_view(template_name = "crud/cargo/actualizar.html"), name='actualizarcargo'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cargo o registro de la Base de Datos 
   
   path('cargo/eliminar/<int:pk>', CargoEliminar.as_view(template_name ='crud/cargo/eliminar.html')), 
   
   
   path('catalogo/', ListadoTipoPlan.as_view(template_name ='plan/catalogo.html'), name='leercatalogo'), 
   path('plan/', ListadoTipoPlan.as_view(template_name ='plan/tables.html'), name='leertipoplan'),
   path('cargo/detalle/<int:pk>', CargoDetalle.as_view(template_name = "crud/cargo/detalle.html"), name='detallecargo'),

  



    
]
