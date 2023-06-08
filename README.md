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

&emsp;&emsp;&emsp;&emsp; - [Modulo Clientes](#modulo-cliente)

&emsp;&emsp;&emsp;&emsp; - [Modulo Empleado](#modulo-empleado)

&emsp;&emsp;&emsp;&emsp; - [Modulo Coordinador](#modulo-coordinador)

&emsp;&emsp;&emsp;&emsp; - [Modulo Servicio](#modulo-servicio)

&emsp;&emsp;&emsp;&emsp; - [Modulo Reserva de Servicio](#modulo-reserva-de-servicio)

&emsp;&emsp;&emsp;&emsp; - [API del Sistema](#api-del-sistema)

&emsp;&emsp;&emsp;&emsp; - [Admin del Proyecto](#admin-del-proyecto)

## *Sobre el Proyecto*
 <br/>
Nuestro proyecto integrador final consiste en el desarrollo de una aplicación web base de reservas de servicios para eventos, la cual permitirá a sus usuarios consultar el catálogo de servicios que la empresa ofrece, y un listado de las reservas realizadas por los clientes. <br /> Esta aplicación permite el registro de empleados, servicios y clientes, asi como la visualización del listado de los mismos. A su vez, es posible acceder a diferentes endpoints con los datos disponibles correspondientes a cada categoría. <br /> Se utilizaron Python/Django como entorno de desarrollo, SQL como base de datos y, las librerias Jinja y Bootstrap.

 <br/>

## *Como ponerlo en marcha localmente ?* 
### Requisitos
* Python 3.9 o versiones recientes
* Django 4.0
* Jinja2
### Instalacion
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
## *Documentacion*
## Modulo Cliente
En este modulo se pueden registrar nuevos clientes, actualizarlos, acceder al listado de clientes activos y eliminar o restaurar registros.

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

 <br/>

## Modulo Empleado
En este modulo se pueden registrar nuevos empleados, actualizarlos, acceder al listado de empleados activos y eliminar o restaurar registros.

 -  [Registrar Empleado](http://127.0.0.1:8000/crear_empleado/)

 <img src="static\img\captures\registrar_empleado.png"/>

 -  [Listado de Empleados](http://127.0.0.1:8000/listar_empleados/)

  <img src="static\img\captures\listar_empleados.png"/>

 Funcionalidades para registros de empleados existentes. A modo de ejemplo:

 -  [Actualizar Empleado 1](http://127.0.0.1:8000/actualizar_empleado/1)

<img src="static\img\captures\actualizar_empleado.png"/>

 -  [Activar Empleado 1](http://127.0.0.1:8000/activar_empleado/1)

<img src="static\img\captures\activar_empleado.png"/>

 -  [Desactivar Empleado 1](http://127.0.0.1:8000/desactivar_empleado/1)

<img src="static\img\captures\desactivar_empleado.png"/>

 <br/>

 ## Modulo Coordinador
En este modulo se pueden registrar nuevos coordinadores, actualizarlos, acceder al listado de coordinadores activos y eliminar o restaurar registros.

 -  [Registrar Coordinador](http://127.0.0.1:8000/crear_coordinador/)

 <img src="static\img\captures\registrar_coordinador.png"/>

 -  [Listado de Coordinadores](http://127.0.0.1:8000/listar_coordinadores/)

  <img src="static\img\captures\listar_coordinadores.png"/>

 Funcionalidades para registros de coordinadores existentes. A modo de ejemplo:

 -  [Actualizar Coordinador 1](http://127.0.0.1:8000/actualizar_coordinador/1)

<img src="static\img\captures\actualizar_coordinador.png"/>

 -  [Activar Coordinador 1](http://127.0.0.1:8000/activar_coordinador/1)

<img src="static\img\captures\activar_coordinador.png"/>

 -  [Desactivar Coordinador 1](http://127.0.0.1:8000/desactivar_coordinador/1)

<img src="static\img\captures\desactivar_coordinador.png"/>
 
 <br/>

 ## Modulo Servicio
En este modulo se pueden registrar nuevos servicios, actualizarlos, acceder al listado de servicios activos y eliminar o restaurar registros.

 -  [Registrar Servicio](http://127.0.0.1:8000/crear_servicio/)

 <img src="static\img\captures\registrar_servicio.png"/>

 -  [Listado de Servicios](http://127.0.0.1:8000/listar_servicios/)

  <img src="static\img\captures\listar_servicios.png"/>

 Funcionalidades para registros de servicios existentes. A modo de ejemplo:

 -  [Actualizar Servicio 1](http://127.0.0.1:8000/actualizar_servicio/1)

<img src="static\img\captures\actualizar_servicio.png"/>

 -  [Activar Servicio 1](http://127.0.0.1:8000/activar_servicio/1)

<img src="static\img\captures\activar_servicio.png"/>

 -  [Desactivar Servicio 1](http://127.0.0.1:8000/desactivar_servicio/1)

<img src="static\img\captures\desactivar_servicio.png"/>
  
 <br/>

 ## Modulo Reserva de Servicio
En este modulo se pueden registrar nuevas reservas servicios, actualizarlas, acceder al listado de reservas activas y eliminar o restaurar registros.

 -  [Registrar Reserva de Servicio](http://127.0.0.1:8000/crear_reserva/)

 <img src="static\img\captures\registrar_reserva.png"/>

 -  [Listado de Reservas de Servicios](http://127.0.0.1:8000/listar_reservas/)

  <img src="static\img\captures\listar_reserva.png"/>

 Funcionalidades para registros de reservas de servicios existentes. A modo de ejemplo:

 -  [Actualizar Reserva de Servicio 1](http://127.0.0.1:8000/actualizar_reserva/1)

<img src="static\img\captures\actualizar_reserva.png"/>

 -  [Eliminar Reserva de Servicio 1](http://127.0.0.1:8000/eliminar_reserva/1)

<img src="static\img\captures\eliminar_reserva.png"/>
 
 <br/>

 ## API del Sistema
 A traves de API es posible la visualización de los diferentes listados correspondientes a los modulos de servicios, clientes, empleados y coordinadores. Permite obtener información de todos los registros del sistema.
 
| Modelo | Endpoint | Descripcion |
| :--- | :--- | :--- |
| Cliente |[Listado de Clientes](http://127.0.0.1:8000/api/clientes/) | Se visualiza el [listado](#endpoint-listado-de-clientes) de todos los clientes|
| Empleados |[Listado de Empleados](http://127.0.0.1:8000/api/empleados/) | Se visualiza el [listado](#endpoint-listado-de-empleados) de todos los empleados|
| Coordinadores |[Listado de Coordinadores](http://127.0.0.1:8000/api/coordinadores/) | Se visualiza el [listado](#endpoint-listado-de-coordinadores) de todos los coordinadores|
| Servicio |[Listado de Servicios](http://127.0.0.1:8000/api/servicios/) | Se visualiza el [listado](#endpoint-listado-de-servicios) de todos los servicios|
| Servicio |api/servicios/<int:id>| Se visualiza un [registro](#endpoint-de-servicio-por-id) de servicio|

`Pantallas:`
### - Endpoint listado de clientes:
<br/>
<img src="static\img\captures\endpoint_clientes.png"/>

### - Endpoint listado de empleados
<br/>
<img src="static\img\captures\endpoint_empleados.png"/>

### - Endpoint listado de coordinadores
<br/>
<img src="static\img\captures\endpoint_coordinadores.png"/>

### - Endpoint listado de servicios
<br/>
<img src="static\img\captures\endpoint_servicios.png"/>

### -Endpoint de servicio por id
<br/>
<img src="static\img\captures\endpoint_serviciosporid.png"/>

## Admin del Proyecto
Desde el [admin de Django](http://127.0.0.1:8000/admin/) es posible acceder y manipular facilmente los registros de una entidad. Para ingresar es necesario contar con credenciales de id, usuario y contraseña de administrador. <br/>En el caso de nuestro proyecto, al ingresar se visualiza la siguiente pantalla:

 <img src="static\img\captures\admin.png"/>

 Desde allí es posible consultar, agregar, modificar y eliminar registros. A su vez, permite filtrar y obtener información de aquellos registros de entidades que cumplan con ciertas condiciones. A continuación se muestra la vista al acceder a Clientes:

  <img src="static\img\captures\admincliente.png"/>