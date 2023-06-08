<p float="left">
<img src="static\img\logo1.jpg" width="100"/>
<img src="static\img\descarga.png"/>
</p>

# DjangoC5S3- Eventos

![Python](https://img.shields.io/badge/Python-3.9-blue?style=plastic&logo=python)
![Django](https://img.shields.io/badge/Django-4.0-green?style=plastic&logo=django)
![Jinja](https://img.shields.io/badge/Jinja2-2.0-red?style=plastic&logo=jinja)

Proyecto Integrador Grupal Squad 3 Comision 5 - Caso de Negocio N° 1  - 
## Desarrolladores
* [Francisco Lopez](https://github.com/panchocdk)
* [Lucas Roman](https://github.com/lucasromanh)
* [Micaela Chaile](https://github.com/micachailee)

## Tabla de contenidos

1. [Sobre el proyecto](#sobre-el-proyecto)
2.  [Como ponerlo en marcha localmente ?](#como-ponerlo-en-marcha-localmentecomo-ponerlo-en-)
3.  [Documentación](#documentación)

&emsp;&emsp;&emsp;&emsp; * [Modulo Clientes](#modulo-clientes)

### Sobre el proyecto
 <br/>
Nuestro proyecto integrador final consiste en el desarrollo de una aplicación web base de reservas de servicios para eventos, la cual permitirá a sus usuarios consultar el catálogo de servicios que la empresa ofrece, y un listado de las reservas realizadas por los clientes. <br /> Esta aplicación permite el registro de empleados, servicios y clientes, asi como la visualización del listado de los mismos. A su vez, es posible acceder a diferentes endpoints con los datos disponibles correspondientes a cada categoría. <br /> Se utilizaron Python/Django como entorno de desarrollo, SQL como base de datos y, las librerias Jinja y Bootstrap.

 <br/>

### Como ponerlo en marcha localmente ? 
#### Requisitos
* Python 3.9 o versiones recientes
* Django 4.0
* Jinja2
#### Instalacion
1.  Clonar este repositorio, desde la terminal escribir:
```
git clone https://github.com/panchocdk/DjangoC5S3-Eventos.git

```
2.  Ir al directorio del proyecto
3.  Crear y activar el entorno virtual
4.  Instalar las dependencias del proyecto
5.  Ejecutar migraciones
```
python manage.py migrate

```
6. Crear superusuario
```
python manage.py createsuperuser

```
7. Ejecutar el servidor 
```
python manage.py runserver

```
### Documentación 
#### Modulo Clientes
En este modulo se puedesn registrar nuevos clientes, actualizarlos, acceder al listado de clientes activos y eliminar o restaurar registros.

 -  [Registrar Cliente](http://127.0.0.1:8000/crear_cliente/)

 <img src="static\img\captures\registrar_cliente.png"/>

 -  [Listado de Clientes](http://127.0.0.1:8000/listar_clientes/)

  <img src="static\img\captures\listar_clientes.png"/>

 Funcionalidades para registros de clientes existentes. A modo de ejemplo:

 -  [Actualizar Cliente 1](http://127.0.0.1:8000/actualizar_cliente/1)

<img src="static\img\captures\actualizar_cliente.png"/>

 -  [Activar Cliente 1](http://127.0.0.1:8000/activar_cliente/1)

<img src="static\img\captures\activar_cliente.png"/>

 -  [Desactivar Cliente 1](http://127.0.0.1:8000/desactivar_cliente/1)

 