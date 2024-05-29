# Extractor de token para acceso API servicios Banco "xxx"
# getJason-rf.PY
# copyright UADER-FCyT-IS2©2024 todos los derechos reservados

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
    def get_jason(self, jsonfile):
        """
        Abre el jsonfile y busca la cuenta con mayor balance para
        descontarle el monto del pedido
        """
        # Abre el json y copia su contenido en data
        with open(jsonfile, "r") as myfile:
            data = myfile.read()

        obj = json.loads(data)
        mayor_balance = 0
        cuenta = ""
        # Busca la cuenta con mayor balance
        for key, value in obj.items():
            if value >= mayor_balance:
                mayor_balance = value
                cuenta = key
        #Si el mayor balance no es >= a 500 no emite el pedido
        if mayor_balance < 500:
            return "Las cuentas no tienen balance suficiente"
        #En caso contrario descuenta el monto
        obj[cuenta] = mayor_balance - 500

        #Reescribe el json con el descuento del monto a la cuenta
        with open(jsonfile, 'w') as file:
            json.dump(obj, file, indent=4)

        return f"Numero pedido: 1, Cuenta: {cuenta}, Monto: {500}, Balance: {mayor_balance-500}"

class Command:
    """
    The Command interface declares a method for executing a command.
    """
    def execute(self):
        pass

class GetJasonCommand(Command):
    """
    Implementa la interfaz Command y encapsula la lógica específica de GetJason.
    """
    def __init__(self, receiver, jsonfile):
        self.receiver = receiver
        self.jsonfile = jsonfile

    def execute(self):
        return self.receiver.get_jason(self.jsonfile)

class Invoker:
    def __init__(self):
        self._commands = {}

    def register(self, name, command):
        self._commands[name] = command

    def execute(self, name):
        if name in self._commands:
            return self._commands[name].execute()
        return "Command not found"

if __name__ == "__main__":
    # Verifica que se ingresó argumento
    if len(sys.argv) != 2:
        print("Error: Faltan ingresar argumentos")
        sys.exit(1)

    # Verifica si se ingresa argumento -v
    if sys.argv[1] == "-v":
        print("Version del programa: 1.2")
        sys.exit(1)

    # Verifica si la extensión es .json
    if not sys.argv[1].lower().endswith('.json'):
        print("Error: El argumento 1 debe tener la extensión .json")
        sys.exit(1)

    # Verifica si el .json existe
    if not os.path.isfile(sys.argv[1]):
        print(f"Error: El archivo '{sys.argv[1]}' no existe")
        sys.exit(1)

    # Instancia la clase GetJason
    getJason = GetJason()
    jsfile = sys.argv[1]

    # Crear el comando y el invocador
    command = GetJasonCommand(getJason, jsfile)
    invoker = Invoker()
    invoker.register("get_json", command)

    # Ejecuta el comando registrado y printea el resultado
    result = invoker.execute("get_json")
    print(result)
