class Car:
    def __init__(self, licencePlate, color, turnedOn):
        self.__licencePlate = licencePlate
        self.__color = color
        self.__turnedOn = turnedOn

    def __str__(self):
        return f"{self.__licencePlate} {self.__color} {self.__turnedOn}"