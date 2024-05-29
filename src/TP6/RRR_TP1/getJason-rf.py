#
#Extractor de token para acceso API servicios Bnaco "xxx"
#getJason-rf.PY
#copyright UADERFCyT-IS2©2024 todos los derechos reservados
#
import json
import sys
import os

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class GetJason(metaclass=SingletonMeta):
    """
    La calse GetJason se encarga de buscar dentro del .json el valor para la clave indica
    El .json y la key se pasan por parametros del metodo getJason()
    """
    def get_jason(self, jsonfile, jsonkey):
        """
        Abre el jsonfile y busca dentro el valor de la clave jsonkey
        Retorna un mensaje de error si la key no se encuentra
        """
        try:
            with open(jsonfile, "r") as myfile:
                data = myfile.read()
            obj = json.loads(data)
            return str(obj[jsonkey])
        except KeyError:
            return f"Error: La clave '{jsonkey}' no se encontró en el archivo JSON."

if __name__ == "__main__":
    # Verifica que se ingresaron 2 argumentos
    if len(sys.argv) != 3:
        if len(sys.argv) == 2 and sys.argv[1] == "-v":
            print("Version del programa: Version 1.1")
        else:
            print("Error: Faltan ingresar argumentos")
        sys.exit()

    # Verifica si la extensión es .json
    if not sys.argv[1].lower().endswith('.json'):
        print("Error: El argumento 1 debe tener la extensión .json")
        sys.exit()

    # Verifica si el .json existe
    if not os.path.isfile(sys.argv[1]):
        print(f"Error: El archivo '{sys.argv[1]}' no existe")
        sys.exit()

    #Se instancia la clase GetJason
    getJason = GetJason()
    jsfile = sys.argv[1]
    jskey = sys.argv[2]
    # Se busca dentro del .json el valor de la key y se printea
    print(getJason.get_jason(jsfile, jskey))