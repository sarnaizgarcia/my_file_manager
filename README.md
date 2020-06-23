# Sistema de gestión de ficheros básico

## Puesta en marcha

1. Crear carpeta del entorno virtual:

```
$ python3 -m venv venv
```

2. Activar venv:

```
$ source venv/bin/activate
```

3. Instalar dependencias:

```
$ pip install -r requirements.txt
```

4. Run the app:

```
$ python main.py
```

Se abrirá la aplicación en

## Descripción de la aplicación

La aplicación consiste en una pantalla de login. Se puede acceder con uno de los usuarios ya creados o registrando uno nuevo en el formulario de registro.

Hay creados los siguientes usuarios:
| id | username | password |
|---|---|---|
| 1 | Silvia | silvia |
| 2 | Roberto | roberto |
| 3 | Adrian | adrian |
| 4 | Ana | ana |
| 5 | Heidi | heidi |

Una vez se ha accedido a la aplicación con usuario y contraseña, la pantalla que aparece es una tabla con los archivos disponibles. Hay cargados algunos archivos de ejemplo.

Se pueden cargar más archivos con el formulario de upload.
Está configurado para aceptar archivos con las siguientes extensiones: '.jpg', '.png', '.pdf', '.txt', '.py' y '.doc'.

Hay dos tipos de usuarios: los que pueden eliminar archivos y los que no.

Tienen permiso para eliminar archivos Silvia y Adrian. El resto sólo los puede descargar. No se pueden duplicar nombres de ficheros.
