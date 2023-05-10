"""Clase para la interaccion con el usuario"""


class Usuario:
    @staticmethod
    def origen(v):
        while True:
            print("Indique el punto de ORIGEN:")
            for i in range(len(v)):
                print(i, v[i])
            n = int(input('Opcion: '))
            if 0 <= n <= len(v) - 1:
                return v[n]
            else:
                print("Opcion invalida")

    @staticmethod
    def destino(v):
        while True:
            print("Indique el punto de DESTINO:")
            for i in range(len(v)):
                print(i, v[i])
            n = int(input('Opcion: '))
            if 0 <= n <= len(v) - 1:
                return v[n]
            else:
                print("Opcion invalida")
