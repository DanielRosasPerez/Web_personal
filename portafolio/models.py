from django.db import models

# Create your models here.
class Project(models.Model): # La clase Project esta heredando de la clase Model.

    # NOTA: CADA QUE AGREGUEMOS UN CAMPO NUEVO A NUESTRO MODELO, DEBEMOS CREAR LA MIGRACIÓN Y MIGRARLA A LA 
    # APLICACIÓN. Es decir:
    # 1. Creamos el campo deseado dentro de esta clase o modelo.
    # 2. Creamos la migración: python manage.py makemigrations <nombre_de_la_app>.
    # 3. Migramos (vaya la redundacia), la migración creada a la aplicación: python manage.py migrate <nombre_de_la_app>.

    title = models.CharField(max_length=200, verbose_name="Título") # Definimos la máxima cantidad de caracteres que puede tener el título.
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    # upload_projects = "<carpeta_de_almacenamiento>", nos sirve para decirle al archivo imagen en donde debe
    # guardarse una vez alguien suba una imagen.
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación") # Se añadirá la hora automáticamente cuando un objeto
    # de esta clase se genere.
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización") # Se añadirá la hora automáticamente cuando el objeto se modifique

    link = models.URLField(verbose_name="Dirección Web", null=True, blank=True)

    class Meta: # Para alterar los metadatos.
        verbose_name = "proyectos_dany_instancias" # Definimos el alias que tendrá la columna de las instancias
        # perteneciente a la clase "Project".

        verbose_name_plural = "proyectos_dany_clase" # Definimos el alias que tendrá la clase.
        
        ordering = ["-created"] # Por default, Django ordena del archivo más antiguo al más reciente,
        # al hacer ordering = ["created"], le decimos a Django que ahora queremos que ordene del archivo
        # más reciente al más antiguo.

    def __str__(self):
        return self.title # De esta manera mostramos el nombre original que le hemos dado a la instancia creada
        # a partir de la clase "Project", en el panel de administrador de Django.