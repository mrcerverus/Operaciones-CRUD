# Operaciones-CRUD

Descripción
Una empresa dedicada al arriendo de inmuebles requiere de su ayuda para crear un sitio web
donde usuarios puedan revisar inmuebles disponibles para el arriendo. Por lo tanto, y ya
habiendo creado un entorno de trabajo y conectado a nuestra base de datos, debemos
continuar en la construcción del proyecto. La siguiente etapa es necesita levantar la
información geográfica de Chile (Comunas y Regiones), además necesita generar un script
que les permita realizar reportes sobre la aplicación.

Hito 1

Requerimientos
1. Instalación de desarrollo, para esto el ambiente de desarrollo debe contar con las
siguientes características:
a. Una instalación de PostgreSQL (link)
b. Creación de un ambiente virtual de Python.
c. Instalación de los paquetes necesarios para la creación de un proyecto de
Django
d. Una aplicación de Django.
(3 Puntos)
2. Definición de modelo de datos para representación del problema utilizando el
framework Django:
a. Representación del modelo relacional de datos.
b. Conección a la base de datos
c. Definición y manejo de llaves primarias en columnas foráneas
(3 Puntos)
3. Implementar operaciones en los modelos para la manipulación de datos utilizando el
framework Django:
a. Crear un objeto con el modelo.
b. Enlistar desde el modelo de datos.
c. Actualizar un registro en el modelo de datos.
d. Borrar un registro del modelo de datos utilizando un modelo Django.
(4 Puntos)


Hito 2

Requerimientos
1. Utilizando las migraciones realice lo siguiente:
a. Poblar la base de datos con todas las regiones y comunas de Chile usando
loaddata. (2 puntos)
b. Poblar de tipos de inmuebles en la base de datos usando loaddata. (2 puntos)
c. Poblar la base de datos con varios inmuebles y usuarios usando loaddata. (1 puntos)
(5 Puntos)
2. Consultar listado de inmuebles para arriendo separado por comunas, solo usando los
campos "nombre" y "descripción" en un script python que se conecta a la DB usando
DJango y SQL guardando los resultados en un archivo de texto.
(3 Puntos)
3. Consultar listado de inmuebles para arriendo separado por regiones en un script
python que se conecta a la DB usando DJango y SQL guardando los resultados en un
archivo de texto.
(2 Puntos)


Hito 3

Requerimientos
1. Crear el template básico que sea página personal de perfil para Arrendatarios y
Arrendadores.
1.1. Generar una vista de login de usuarios.
1.2. Generar una vista de registro.
1.3. Realizar redireccionamiento de urls.
1.4. Desplegar los datos del usuario.
(8 Puntos)
2. Agregar a la página personal de un Arrendatario y Arrendador la posibilidad de
modificar sus datos personales.
(2 Puntos)

Hito 4

Requerimientos
1. Crear página web básica donde arrendadores puedan agregar nuevos inmuebles.
a. Generar las rutas para la vista para agregar nuevas viviendas.
b. Generar el objeto de formulario.
c. Agregar la función para guardar el objeto.
(4 Puntos)
2. Crear página web básica donde arrendadores puedan actualizar/borrar un inmueble
existente.
a. Generar las rutas para la vista para actualizar las viviendas por usuario.
b. Generar el objeto de formulario en base a él modelo definido.
c. Agregar la función para actualizar el objeto.
(4 Puntos)
3. Crear una página web básica donde los arrendatarios puedan ver la oferta disponible.
a. Generar las rutas para ver las viviendas.
b. Crear la vista y el controlador que le permitan enlistar las viviendas.
(2 Puntos)
