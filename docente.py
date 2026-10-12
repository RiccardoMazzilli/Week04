from persona import Persona
# Per dire che la classe Docente EREDITA da Persona
# devo inserire il nome della classe tra ( )

class Docente(Persona):
    def __init__(self, nome, cognome, dipartimento):
        # SBAGLIATO RIPETERE LA DEFINIZIONE DI ATTRIBUTI DEL PADRE
        #self.__nome = nome
        #self.__cognome = cognome
        super().__init__(nome, cognome)   # Costruisce "la parte" Persona del Docente

        # POI INIZIALIZZO GLI ATTRIBUTI SPECIFICI DEL DOCENTE
        self.dipartimento = dipartimento

