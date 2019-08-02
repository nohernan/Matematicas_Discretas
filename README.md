# Matemáticas Discretas. Licenciatura en Ciencias de Datos. IIMAS, UNAM.

Página del curso [aquí](https://sites.google.com/view/mat-discretas-201/).

## Haskell
_Haskell_ es un lenguaje de programación funcional puro y perezoso, cuyos tipos son determinados estáticamente de manera polifórmica. Más información en el [wiki oficial](https://wiki.haskell.org/). 

### Instalación de Haskell

_Haskell_ se utilizará en el laboratorio de manera ocasional. Se recomienda instalar `stack` para correr programas en Haskell. En Ubuntu 18.04 `stack` se instala ejecutando el siguiente comando en una terminal:

`$ wget -qO- https://get.haskellstack.org/ | sh`

Para verificar que la instalación fue correcta se ejecuta el comando `stack --version`, la respuesta esperada debe ser algo como `Version 2.1.3, Git revision 636e3a759d51127df2b62f90772def126cdf6d1f (7735 commits) x86_64 hpack-0.31.2`. La instrucción para instalar  _haskell stack_ se tomó de este [enlace](https://docs.haskellstack.org/en/stable/README/#how-to-install).

Si surge el error `<command line>: can't load .so/.DLL for: libgmp.so (libgmp.so: cannot open shared object file: No such file or directory)`, hay que instalar `libgmp3-dev` con el comando `$ sudo apt install libgmp3-dev`.

---

## Python
_Python_ es un lenguaje de programación de alto nivel, orientado a objetos, interpretado con semántica dinámica. Sus estructuras de datos de alto nivel integradas, combinadas con su tipificación dinámica y ligado dinámico, hace a este lenguaje muy atractivo para el Desarrollo de Aplicaciones Rápido, así como para su uso como lenguaje _script_ o adhesivo para conectar componentes existentes. La sintaxis sencilla y fácil de aprender de _Python_ enfatiza legibilidad y por lo tanto reduce su costo de mantenimiento. _Python_ suporta módulos y paquetes, y fomenta la modularidad de programas y el reuso del código. 

### Instalación de Python

Para el curso usaremos python 3.7 que se instala con las instrucciones siguientes desde una terminal en Ubuntu 18.04. 

1. `$ sudo apt-get install build-essential checkinstall`
1. `$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev`
1. `$ cd /usr/src`
1. `$ sudo wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz`
1. `$ sudo tar xzf Python-3.7.3.tgz`
1. `$ cd Python-3.7.3`
1. `$ sudo ./configure --enable-optimizations`
1. `$ sudo make altinstall`

Para verificar que la instalación fue exitosa hay que ejecutar la siguiente instrucción en una terminal: `$ python3.7 -V`, que debe arrojar `Python 3.7.3`. Las instrucciones anteriores fueron tomadas de [este enlace](https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/).

