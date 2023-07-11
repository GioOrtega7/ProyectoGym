# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cargo(models.Model):
    idcargo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargo'


class Cita(models.Model):
    idcita = models.IntegerField(primary_key=True)
    horacita = models.IntegerField(blank=True, null=True)
    fecha = models.IntegerField(blank=True, null=True)
    notas = models.CharField(max_length=45, blank=True, null=True)
    persona_idpersona = models.IntegerField()
    estado_idestado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cita'


class Dia(models.Model):
    iddia = models.IntegerField(primary_key=True)
    dia = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dia'


class Dieta(models.Model):
    iddieta = models.IntegerField(primary_key=True)
    idempleado = models.CharField(max_length=45, blank=True, null=True)
    planificacion_idplanificacion = models.IntegerField()
    receta_idreceta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dieta'


class Ejercicio(models.Model):
    idejercicio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    imagen = models.CharField(max_length=45, blank=True, null=True)
    enfoque_idenfoque = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ejercicio'


class Enfoque(models.Model):
    idenfoque = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enfoque'


class Estado(models.Model):
    idestado = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'


class Evolucion(models.Model):
    idevolucion = models.IntegerField(primary_key=True)
    medida_idmedida = models.IntegerField()
    rutina_idrutina = models.IntegerField()
    dieta_iddieta = models.IntegerField()
    fecha = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evolucion'


class Genero(models.Model):
    idgenero = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genero'


class Historia(models.Model):
    idhistoria = models.IntegerField(primary_key=True)
    evolucion_idevolucion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'historia'


class Horario(models.Model):
    idhorario = models.IntegerField(primary_key=True)
    fecha = models.CharField(max_length=45, blank=True, null=True)
    horainicio = models.CharField(max_length=45, blank=True, null=True)
    horafin = models.CharField(max_length=45, blank=True, null=True)
    cita_idcita = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'horario'


class Ingrediente(models.Model):
    idingrediente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    racion = models.IntegerField()
    ingredientescol = models.CharField(max_length=45, blank=True, null=True)
    proteinas = models.FloatField(blank=True, null=True)
    carbohidratos = models.FloatField(blank=True, null=True)
    calorias = models.FloatField(blank=True, null=True)
    grasas = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingrediente'


class Medida(models.Model):
    idmedida = models.IntegerField(primary_key=True)
    estatura = models.FloatField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    indicegrasa = models.IntegerField(blank=True, null=True)
    imc = models.FloatField(db_column='IMC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medida'


class Ocupacion(models.Model):
    idocupacion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocupacion'


class Persona(models.Model):
    idpersona = models.IntegerField(primary_key=True)
    nombre1 = models.CharField(max_length=45, blank=True, null=True)
    nombre2 = models.CharField(max_length=45, blank=True, null=True)
    apellido1 = models.CharField(max_length=45, blank=True, null=True)
    apellido2 = models.CharField(max_length=45, blank=True, null=True)
    numid = models.CharField(max_length=45, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    direccion = models.IntegerField(blank=True, null=True)
    genero_idgenero = models.IntegerField()
    tipodocumento_idtipodocumento = models.IntegerField()
    cargo_idcargo = models.IntegerField()
    usuario_idusuario = models.IntegerField()
    tipopersona_idtipopersona = models.IntegerField()
    ocupacion_idocupacion = models.IntegerField()
    plan_idmembresia = models.IntegerField()
    historia_idhistoria = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'persona'


class Plan(models.Model):
    idmembresia = models.IntegerField(primary_key=True)
    fechainicio = models.IntegerField(blank=True, null=True)
    fechafin = models.IntegerField(blank=True, null=True)
    tipoplan_idtipoplan = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'plan'


class Planificacion(models.Model):
    idplanificacion = models.IntegerField(primary_key=True)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planificacion'


class Receta(models.Model):
    idreceta = models.IntegerField(primary_key=True)
    imagen = models.CharField(max_length=45, blank=True, null=True)
    preparacion = models.CharField(max_length=45, blank=True, null=True)
    carbohidratos = models.FloatField(blank=True, null=True)
    calorias = models.FloatField()
    grasas = models.FloatField(blank=True, null=True)
    tipoalimento_idtipoalimento = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'receta'


class Repeticion(models.Model):
    idrepeticion = models.IntegerField(primary_key=True)
    cantidad = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repeticion'


class Rutina(models.Model):
    idrutina = models.IntegerField(primary_key=True)
    dia_iddia = models.IntegerField()
    ejercicio_idejercicio = models.IntegerField()
    serie_idserie = models.IntegerField()
    repeticion_idrepeticion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rutina'


class Serie(models.Model):
    idserie = models.IntegerField(primary_key=True)
    cantidad = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serie'


class Tipoalimento(models.Model):
    idtipoalimento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    verduras = models.CharField(max_length=45, blank=True, null=True)
    granos = models.CharField(max_length=45, blank=True, null=True)
    ensaladas = models.CharField(max_length=45, blank=True, null=True)
    bebidas = models.CharField(max_length=45, blank=True, null=True)
    frutas = models.CharField(max_length=45, blank=True, null=True)
    ingrediente_idingrediente = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipoalimento'


class Tipocomida(models.Model):
    idtipocomida = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    desayuno = models.CharField(max_length=45, blank=True, null=True)
    almuerzo = models.CharField(max_length=45, blank=True, null=True)
    mediatarde = models.CharField(max_length=45, blank=True, null=True)
    cena = models.CharField(max_length=45, blank=True, null=True)
    entrenoche = models.CharField(max_length=45, blank=True, null=True)
    ingrediente_idingrediente = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipocomida'


class Tipodocumento(models.Model):
    idtipodocumento = models.IntegerField(primary_key=True)
    tipodoc = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipodocumento'


class Tipopersona(models.Model):
    idtipopersona = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipopersona'


class Tipoplan(models.Model):
    idtipoplan = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    precio = models.CharField(max_length=45, blank=True, null=True)
    foto = models.ImageField(upload_to="img/")

    class Meta:
        managed = False
        db_table = 'tipoplan'


class Usuario(models.Model):
    idusuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    clave = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
