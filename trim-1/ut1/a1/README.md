# UT1-A1: Mis series favoritas

## Introducción

Vamos a utilizar nginx para alojar una página web que muestre nuestras series favoritas. El nombre de la página será `alejandro.me` y nos mostrará las imágenes de las series al entrar en `alejandro.me/series/`.

## Desarrollo

* Lo primero es añadir `alejandro.me` al fichero `/etc/hosts`, para facilitar el acceso a la web.

![](img/1.png)

* Una vez hecho eso, creamos la carpeta `/var/www/html/series` donde estará ubicado el index.html que mostrará nuestra página. A continuación, añadimos el virtualhost en el fichero `/etc/nginx/sites-available/alejandro.me` con la siguiente configuración:

![](img/4.png)

* Para que la configuración del fichero funcione, tendremos que crear un enlace simbólico al mismo en `/etc/nginx/sites-enabled` con el comando `ln -s`. 

* Configuramos el index.html ubicado en `/var/www/html/series` de la siguiente forma:

![](img/7.png)

> NOTA:
    Para pasar las imágenes al servidor, podemos descargarlas en la máquina cliente y utilizar el comando `scp` de la siguiente forma:

    ![](img/5.png)
      