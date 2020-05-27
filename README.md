# Examen para desarrollador python.

_Proyecto para evaluacion de posición desarrollador python, el sistema se divide en las siguientes aplicaciones_

* Pacientes. Aplicacion que realiza las operaciones realacionadas a los pacientes (crear, leer y editar).
* Citas. Aplicacion que realizar acciones relacionadas con las citas.
* Medicos. Aplicacion que realizar acciones operaciones realacionadas a los medicos (crear, leer y editar).
* Consultorios. Aplicacion que realizar acciones operaciones realacionadas a los consultorios (crear, leer y editar).
* Mensajes. Aplicacion que realizar acciones operaciones realacionadas al envio de mensajes.

_Para mayor informacion acerca de los enpoints, su funcionamiento y ejemplos re respuesta consultar la siguiente 
[documentacion](https://documenter.getpostman.com/view/7570622/SztA79JP?version=latest)_

_El proyecto se conforma de dos secciones principales la seccion de api, cuyas url vienen acompañadas con el 
prefijo api y una capa de Front para visuqlizar los datos de manera más sencilla cuyas url vienen acompañadas 
del prefijo front_

## Comenzando 

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu 
máquina local para propósitos de desarrollo_


### Pre-requisitos 

_Se utilizara Docker como herramienta para correr la aplicacion, por lo que será necesario contar con docker_


### Instalación 

_Una vez instalado docker y el repositorio en su maquina local debera ejecutar el en linea de comandos en la
raiz de este proyecto el comando docker-compose up, lo cual realizara las descargas necesarias de las imagenes y 
las dependencias requeridas por el proyecto._

_Una vez levantado el servidor la aplicacion correra en el puerto 8000_


## Tests

_Para ejecutar los tests de la aplicacion es necesario correr el siguiente comando:_

_python manage.py test_

_Lo cual ejecutara 24 test relacionados con la creacion, listado y actualizacion de los diferentes modelos en 
la base de datos_


## Recomendaciones

* Al realizar deploy en ambiente productivo será necesario cambiar la base de datos

## Importante

* SECRET_KEY deberá ser colocada como variable de ambiente en produccion para dejarla fuera
del archivo settings

* DJANGO_SETTINGS_MODULE en produccion deberá ser colocada como variable de ambiente con el
valor podemosExam.settings.prod


## Autores 

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Victor Hugo Herver Segura** - *Trabajo Inicial* - [VictorHerver](https://github.com/VictorHerver)  - [vicherver](https://gitlab.com/vicherver)


