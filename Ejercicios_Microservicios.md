## Microservicios. Ejercicios.

#### Ejercicio 1. Realizar una aplicación básica que use express para devolver alguna estructura de datos del modelo que se viene usando en el curso.

Como mi proyecto se está desarrollando en Python creo que es más conveniente realizar estos ejercicios en el mismo lenguaje para que posteriormente pueda aplicar los conocimientos adquiridos y llevar a cabo los hitos. En este caso un *framework* similar a express es *Flask*, con el cual se pueden desarrollar microservicios en Python. Para este ejercicio he reutilizado el microservicio del hito 3 que es capaz de conectarse a la API Petfinder y descargar datos sobre veinte mascotas para posteriormente visualizarlos en formato *JSON*. La implementación ser puede encontrar en el siguiente [fichero.](https://github.com/lidiasm/EjerciciosCC/blob/master/src/rest.py)
Un ejemplo de su funcionamiento se puede comprobar a continuación, en el que conectamos con la API Petfinder de forma satisfactoria y posteriormente nos descargamos los datos accediendo a la segunda ruta.

![Probando microservicio ejercicio 1.](https://github.com/lidiasm/EjerciciosCC/blob/master/imagenes/REST%20descargar%20datos.png)

#### Ejercicio 2. Programar un microservicio en express (o el lenguaje y marco elegido) que incluya variables como en el caso anterior.

Para este ejercicio se va a implementar un servicio REST capaz de insertar una organización de adopción de mascotas. Por lo tanto el servicio será PUT y se le deberán pasar como parámetros el nombre de la organización, la ciudad y el país en el que reside. Para ello se implementará un método en la clase *Mascotas* que se encargue de añadir la nueva organización que se le pase como argumento, y el servicio REST hará uso de dicho método con el fin de separar la lógica de negocio de la aplicación de los servicios REST. A continuación se pueden observar las implementaciones anteriores para la [clase *Mascotas*](https://github.com/lidiasm/EjerciciosCC/blob/master/src/mascotas.py) y para el [*microservicio*](https://github.com/lidiasm/EjerciciosCC/blob/master/src/rest.py).

Para ejecutarlo en primer lugar levantaremos el servidor de *Flask* y a continuación realizamos la petición mediante *curl* tal y como se puede comprobar en las siguientes capturas. Si los parámetros han sido correctos y se ha podido insertar la nueva organización, como es en este caso, se devolverán los datos de las organizaciones registradas. Como solo hemos añadido una organización con la petición actual el resultado es un *JSON* con sus correspondientes datos.

![Servidor Flask.](https://github.com/lidiasm/EjerciciosCC/blob/master/imagenes/Ejecutar%20servidor%20Flask.png)

![Resultado PUT.](https://github.com/lidiasm/EjerciciosCC/blob/master/imagenes/PUT%20rest.png)

#### Ejercicio 3. Crear pruebas para las diferentes rutas de la aplicación.

Para probar el correcto funcionamiento de los servicios REST se han implementado un conjunto de tests que se pueden visualizar en este [fichero](https://github.com/lidiasm/EjerciciosCC/blob/master/tests/test_rest.py). Dichos servicios REST corresponden a las principales acciones que se pueden realizar tales como conectarse a la API Petfinder, descargar datos de mascotas así como registrar nuevas organizaciones.

#### Ejercicio 4. Experimentar con diferentes gestores de procesos y servidores web front-end para un microservicio que se haya hecho con antelación, por ejemplo en la sección anterior.

En este ejercicio se realizarán pruebas con el WSGI *Green Unicorn* puesto que es el más adecuado tanto para gestionar los procesos como para levantar el microservicio puesto que el desarrollo se está realizando en Python. Para ejecutar *Gunicorn* y levantar así el microservicio he utilizado la orden `pipenv run gunicorn --chdir src rest:app -p pid_gunicorn.pid -D -b :${PUERTO}` cuyo funcionamiento consiste en cambiar al directorio donde se encuentran los ficheros de implementación tanto de la lógica de la aplicación como el del microservicio para ejecutarlo en el puerto que indique la variable de entorno que previamente se ha debido de definir en el sistema. Con la opción *-D* indicamos que se ejecute en seguno plano para que no bloquee la consola y con la opción *-p* escribe el identificador del proceso del servidor en el fichero *pid_gunicorn.pid*, que posteriormente utilizaremos para finalizar su ejecución sin necesidad de incluir un gestor de procesos adicional.

A continuación se presentan algunas capturas probando el microservicio ejecutado mediante *Gunicorn*. En la primera captura hacemos uso del servicio REST que conecta con la API Petfinder.

![Conexión API.](https://github.com/lidiasm/EjerciciosCC/blob/master/imagenes/REST%20conectar%20api.png)

Una vez se ha realizado la conexión correctamente procedemos a descargarnos datos de hasta veinte mascotas.

![Descarga datos mascotas.](https://github.com/lidiasm/EjerciciosCC/blob/master/imagenes/REST%20descargar%20datos.png)

Por último probamos el servicio que añade una nueva organización mediante *curl* puesto que el verbo *PUT* no es accesible mediante URL.

![Añadir nueva organización.](https://github.com/lidiasm/EjerciciosCC/blob/master/imagenes/REST%20PUT%20organizaci%C3%B3n.png)

#### Ejercicio 5. Usar rake, invoke o la herramienta equivalente en tu lenguaje de programación para programar diferentes tareas que se puedan lanzar fácilmente desde la línea de órdenes.

Como en los hitos 2 y 3 para este ejercicio también he utilizado como herramienta de construcción *make* por su sencillez a la hora de utilizarla, por la experiencia que tengo usandola durante el grado además de por su independencia del lenguaje. Las diferentes tareas automatizadas que he desarrollado consisten en crear un entorno virtual con *Python* 3 así como la instalación de las dependencias necesarias para la aplicación, como *petpy*, para el microservicio, como *Flask* y *Gunicorn*, además de *pytest* para ejecutar los tests de este último. Todas ellas se recogen en el fichero [*requirements.txt*](https://github.com/lidiasm/EjerciciosCC/blob/master/requirements.txt). El fichero [*makefile*](https://github.com/lidiasm/EjerciciosCC/blob/master/Makefile) contiene comentarios explicativos para cada una de las tareas automáticas comentadas anteriormente.
