## Contenedores. Ejercicios.

### Ejercicios 2 y 7. Tomar algún programa simple, “Hola mundo” impreso desde el intérprete de línea de órdenes, y comparar el tamaño de las imágenes de diferentes sistemas operativos base, Fedora, CentOS y Alpine, por ejemplo. Reproducir los contenedores creados anteriormente usando un Dockerfile.

El código fuente del programa *Hola mundo* en Python se puede encontrar en este [fichero](https://github.com/lidiasm/EjerciciosCC/blob/master/src/hola_mundo.py). Para construir los diversos contenedores he generado un fichero *dockerfile* que se puede visualizar [aquí](https://github.com/lidiasm/EjerciciosCC/blob/master/Dockerfile). En función del sistema base con el que queramos construir el contenedor descomentaremos una línea *FROM* u otra.

Tras construir el contenedor utilizando los tres sistemas operativos base anteriores, a continuación se muestra una captura acerca de los tamaños de cada uno de ellos.

![Tamaños contenedores.](https://github.com/lidiasm/EjerciciosCC/blob/master/imagenes/Tama%C3%B1os.png)

Tal y como se puede comprobar el tamaño del contenedor que utiliza *Alpine* como sistema base es mucho menor que los contenedores que utilizan cualquiera de los dos sistemas operativos. Por lo tanto, esto afirma que el sistema operativo *Alpine* destaca, principalmente, por su ligereza.

### Ejercicio 3. Crear a partir del contenedor anterior una imagen persistente con commit.

Para realizar este ejercicio utilizaremos el último contenedor que se ha ejecutado del ejercicio anterior, que en mi caso es el que tiene como base al sistema *CentOS*. Una vez conocemos su identificador ejecutamos la orden `commit` sobre él para crear una imagen persistente llamada `hola_mundo_centos_commit`. Tal y como se puede comprobar en la siguiente captura, tras ejecutar este comando nos devuelve un *sha* concreto que lo identifica unívocamente.

![Commit.](https://github.com/lidiasm/EjerciciosCC/blob/master/imagenes/Docker%20commit.png)

