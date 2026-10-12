


class Persona:
    def __init__(self, nome, cognome):
        self.__nome = nome
        self.__cognome = cognome

    def __str__(self):
        return f"{self.__nome} {self.__cognome}"


p1 = Persona("Mario", "Rossi")
p2 = Persona("Luigi", "Neri")