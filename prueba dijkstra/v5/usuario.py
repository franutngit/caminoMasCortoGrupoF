"""Clase para la interaccion con el usuario"""


class Usuario:
    @staticmethod
    def origen(vertices):
        while True:
            print("Indique el punto de ORIGEN:")
            for i in range(len(vertices)):
                print(i, vertices[i])
            opcion = int(input('Opcion: '))
            if 0 <= opcion <= len(vertices) - 1:
                return vertices[opcion]
            else:
                print("Opcion invalida")

    @staticmethod
    def destino(vertices):
        while True:
            print("Indique el punto de DESTINO:")
            for i in range(len(vertices)):
                print(i, vertices[i])
            opcion = int(input('Opcion: '))
            if 0 <= opcion <= len(vertices) - 1:
                return vertices[opcion]
            else:
                print("Opcion invalida")
