# Primer sistema a probar: Alpine
# FROM python:3.6-alpine
# Segundo sistema a probar: Fedora
# FROM fedora
# Tercer sistema a probar: CentOS
FROM centos

# Establecemos el directorio de trabajo del ejercicio.
WORKDIR Escritorio/CC/ContenedoresEjercicio2

# SOLO ES NECESARIO PARA CENTOS.
# Instalamos Python 3.6.
RUN dnf -y install python36

# Copiamos el fichero fuente al directorio de trabajo.
COPY src/hola_mundo.py ./

# Ejecutamos el programa desde la shell de Python3.
CMD ["python3", "./hola_mundo.py"]