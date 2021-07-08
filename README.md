# Jaguarete Kaa S.A
## Tienda de productos

Trabajo final de tienda de productos de Jaguarete Kaa S.A del curso de Django de Polotic de Misiones.

## Pasos

1- Crear ambiente de Python con virtualenv o similar y procedemos a conseguir todos los paquetes.
```sh
pip install -r requirements.txt
```
2- Generamos las migraciones.
```sh
python manage.py makemigrations
```
3- Corremos migraciones en base de datos.
```sh
python manage.py migrate
```
4- Crear grupos con este script.
```sh
python manage.py shell < create_groups.py
```
5- Creamos superusuario o procedemos a registrarnos.
```sh
python manage.py shell < create_groups.py
```
