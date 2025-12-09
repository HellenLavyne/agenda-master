from enum import Enum


class Identificador(Enum):
    CELULAR = ("Celular")
    CASA = ("Casa")
    TRABALHO = ("Trabalho")

    def __init__(self, nome:str):
        self.identificador = nome

    def __str__(self):
        # Retorna o nome do identificador (ex: "Celular").
        return self.identificador
