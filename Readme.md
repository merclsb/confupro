# CONFUPRO

Trabajo fin de grado del Curso de Adaptación al grado de Ingenieria Informática

![Unir Logo](https://www.decointerior.es/wp-content/uploads/2015/01/logo-unir-e1423826671421.png)

![](http://cud.unizar.es/sites/default/files/personal/pers_asanchez/ListadoAnalisis.png)

![](http://cud.unizar.es/sites/default/files/personal/pers_asanchez/ResultadoFuncional.png)

# Pasos para la instalación

```
mkdir confupro && cd confupro/

virtualenv -p python3.4 .

source bin/activate

pip install -r requisitos.txt

django-admin.py startproject website && mv website src && cd src

./manage.py migrate

./manage.py startapp confupro

http://127.0.0.1:8000/

http://127.0.0.1:8000/admin

```
