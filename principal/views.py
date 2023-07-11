# librerias del CRUD
from django.shortcuts import render
from principal.models import * #con opcion de quitar pricipal
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Habilitamos los mensajes para class-based views  
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
# Habilitamos el uso de mensajes en Django
from django.contrib import messages
# Habilitamos los formularios en Django
from django import forms 


# Create your views here.

def Login(request):
    return render (request, "login.html")

def Home(request):
    return render(request, "index.html")

def Parametros (request):
    return render (request, "crud/index.html")

class ListadoTipodocumento(ListView):
     model = Tipodocumento


class TipodocumentoCrear(SuccessMessageMixin, CreateView):
    model =Tipodocumento
    form = Tipodocumento
    fields = "__all__"
    success_message ='Tipodocumento creada correctamente'
     
    def get_success_url(self):        
        return reverse('leertipodoc') # Redireccionamos a la vista principal 'leer'

class TipodocumentoDetalle (DetailView):
    model =Tipodocumento

class  TipodocumentoActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipodocumento
    form = Tipodocumento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leertipodoc') # Redireccionamos a la vista principal 'leer'


class TipodocumentoEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipodocumento 
    form = Tipodocumento
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'tipo documento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))      
        return reverse("leertipodoc") # Redireccionamos a la vista principal 'leer'






class ListadoCargo(ListView):
     model = Cargo
     form = Cargo
     fields = "__all__"

     success_message ='Regional creado correctamente'
     def get_success_url(self):        
        return reverse('principal:leercargo') # Redireccionamos a la vista principal 'leer' 




class CargoDetalle (DetailView):
    model =Cargo

class  CargoActualizar(SuccessMessageMixin,UpdateView):
    model =  Cargo
    form = Cargo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Cargo Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leercargo') # Redireccionamos a la vista principal 'leer'


class CargoEliminar(SuccessMessageMixin, DeleteView): 
    model = Cargo 
    form = Cargo
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Cargo Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))      
        return reverse("principal:leercargo") # Redireccionamos a la vista principal 'leer'
    


    #VISTA PARA PLAN PRUEBA


     

class TipoPlanDetalle (DetailView):
    model =Tipoplan

class ListadoTipoPlan (SuccessMessageMixin, CreateView, ListView):
     model = Tipoplan
     form = Tipoplan
     fields = "__all__"

     success_message ='Regional creado correctamente'
     def get_success_url(self):        
        return reverse('principal:leertipoplan') # Redireccionamos a la vista principal 'leer' 