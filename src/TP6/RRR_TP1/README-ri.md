# Extractor de Token para Acceso API Servicios Banco "xxx"

## Descripción
Este programa se encarga de extraer el token necesario para acceder a los servicios API del banco "xxx". El programa busca dentro de un archivo JSON (`sitedata.json`) el valor asociado a una clave específica y realiza un pedido de pago de $500 desde la cuenta con el mayor balance.

## Archivos del Proyecto

- **getJason-ri.py**: Script principal que realiza la extracción del token y el pedido de pago.
- **README.md**: Archivo de documentación del proyecto.
- **COMPILE.sh**: Script para compilar los archivos.
- **sitedata.json**: Archivo JSON que contiene dos tokens (`token1` y `token2`) y sus valores.

## Uso

Para ejecutar el programa, usa el siguiente comando en la terminal:
"python getJason-ri.py sitedata.json"

## Argumentos
- **sitedata.json**: Archivo JSON que contiene las cuentas y sus balances.

## Ejemplo
python getJason-ri.py sitedata.json

Este comando procesará el archivo sitedata.json, buscará la cuenta con el mayor balance y descontará $500 de dicha cuenta. El resultado será impreso en la terminal.

## Características
    - **Singleton Pattern**: La clase principal utiliza el patrón de diseño Singleton para asegurar que solo haya una instancia del objeto que maneja el archivo JSON.
    - **Command Pattern**: Se implementa el patrón de diseño Command para encapsular la lógica de negocio y facilitar la ejecución de comandos.
    - **Versión**: Si el programa se ejecuta con el argumento -v, mostrará la versión actual del programa.

## Manejo de Errores
    -Si no se proporciona un archivo JSON como argumento, el programa mostrará un mensaje de error y terminará la ejecución.
    -Si el archivo proporcionado no tiene la extensión .json, el programa mostrará un mensaje de error y terminará la ejecución.
    -Si el archivo JSON no existe, el programa mostrará un mensaje de error y terminará la ejecució n.
    -Si el mayor balance en el archivo JSON es menor a $500, el programa devolverá un mensaje indicando que las cuentas no tienen balance suficiente.

## Versión
Este programa está en la versión 1.2. Para mostrar la versión del programa, puedes ejecutar el siguiente comando:
"python getJason-ri.py -v"