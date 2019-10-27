## Desarrollo basado en pruebas. Ejercicios.

#### Ejercicio 1. Instalar alguno de los entornos virtuales de node.js (o de cualquier otro lenguaje con el que se esté familiarizado) y, con ellos, instalar la última versión existente, la versión minor más actual de la 4.x y lo mismo para la 0.11 o alguna impar (de desarrollo).

Debido a que el proyecto en esta asignatura se desarrollará en Python realizaré este ejercicio también en este lenguaje. Para crear entornos virtuales Python dispone de la biblioteca [**virtualenv**](https://virtualenv.pypa.io/en/latest/installation/) y para instalarla en Ubuntu basta con ejecutar el comando que se aprecia en la siguiente captura.

![Instalación de virtualenv en Ubuntu](https://github.com/lidiasm/EjerciciosCC/blob/master/imagenes/Instalando%20virtualenv.png)

Para crear el primer entorno virtual usando la biblioteca instalada anteriormente ejecuto el comando *virtualenv -p* para especificar el directorio donde se encuentra la versión de Python que estará disponible en dicho entorno. En mi caso será la versión 3.6.9, tal y como se puede comprobar en la siguiente captura.

![Entorno virtual 1 con Python3.](https://github.com/lidiasm/EjerciciosCC/blob/master/imagenes/entornov1%20con%20python3.png)

Para el segundo entorno virtual utilizaré una versión más antigua e impar como es la 2.7.

![Entorno virtual 2 con Python2](https://github.com/lidiasm/EjerciciosCC/blob/master/imagenes/entornov2%20con%20python2.png)

#### Ejercicio 2. Crear una descripción del módulo usando package.json. En caso de que se trate de otro lenguaje, usar el método correspondiente.

En el caso del lenguaje Python existen diversos manejadores de paquetes pero el que viene instalado por defecto es [*pip*](https://pip.pypa.io/en/stable/quickstart/). Para especificar un listado de dependencias usando esta librería es necesario crear un fichero *requirements.txt* donde detallar los comandos necesarios para instalar todas las dependencias requeridas. Dependiendo de si el lenguaje es Python3 o inferior habrá que utilizar el comando *pip3* o *pip*, respectivamente. En el primer caso para instalar SQLite se debe incluir el comando ***pip3 install sqlite3*** en el fichero .txt aunque con Python3 ya viene instalada por defecto.

#### Ejercicio 3. Descargar el repositorio de ejemplo anterior, instalar las herramientas necesarias (principalmente Scala y sbt) y ejecutar el ejemplo desde sbt. Alternativamente, buscar otros marcos para REST en Scala tales como Finatra o Scalatra y probar los ejemplos que se incluyan en el repositorio.

En primer lugar descargo el repositorio desde la línea de órdenes con el comando *git clone*.

![Descarga repositorio.](https://github.com/lidiasm/EjerciciosCC/blob/master/imagenes/Clonando%20repo.png)

A continuación instalo y configuro *Java 8* puesto que es un requisito previo a la instalación de *Scala*.

![Instalación de Java 8.](https://github.com/lidiasm/EjerciciosCC/blob/master/imagenes/Java8.png)

Posteriormente se instala [*Scala* y *sbt*](http://www.codebind.com/linux-tutorials/install-scala-sbt-java-ubuntu-18-04-lts-linux/) también mediante comandos. Continuamos siguiendo las instrucciones que se encuentran en el *README* del repositorio descargado para iniciar *sbt*, compilar y ejecutar el proyecto. Una vez hecho nos dirigimos a la dirección *http://localhost:8080* para comprobar que la aplicación se está ejecutando. Si es así aparecerá una pantalla del siguiente estilo.

![Ejecución de la aplicación.](https://github.com/lidiasm/EjerciciosCC/blob/master/imagenes/Localhost.png)

A continuación realizamos las pruebas recomendadas en el repositorio cuyos resultados pueden observarse en la siguiente captura.

![Pruebas.](https://github.com/lidiasm/EjerciciosCC/blob/master/imagenes/Pruebas.png)

Tal y como se puede comprobar el objetivo de las pruebas consiste en añadir diversas apuestas a un diccionario de porras especificando el nombre de la persona que apuesta y su resultado mediante uno de los verbos del protocolo HTTP: el verbo *PUT*. En la siguiente captura se puede comprobar cómo se van añadiendo los elementos uno a uno al diccionario.

![Resultados de las pruebas.](https://github.com/lidiasm/EjerciciosCC/blob/master/imagenes/Resultados.png)