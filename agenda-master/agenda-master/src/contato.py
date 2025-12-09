from src.fone import Fone
from typing import List, Optional

class Contato:

    def __init__(self, nome: str):
        # Inicializa um contato com um nome e uma lista vazia de Fones.
        self._nome = nome
        self._fones: List[Fone] = []

    def getName(self) -> str:
        # Retorna o nome do contato.
        return self._nome

    def getQuantidadeFones(self) -> int:
        # Retorna o número de fones cadastrados no contato.
        return len(self._fones)

    def getFones(self) -> list:
        """ Retorna a lista de objetos Fone.
        Retorna uma cópia para evitar modificações externas diretas na lista interna."""
        return self._fones.copy()

    def adicionarFone(self, fone: Fone) -> bool:
        if not Fone.validarNumero(fone.getNumero()):
            return False

        if fone in self._fones:
            return False

        self._fones.append(fone)
        return True

    def removerFone(self, index: int) -> bool:
        """ Remove um fone pelo seu índice na lista."""
        if 0 <= index < len(self._fones):
            # Remove o item pelo índice
            del self._fones[index]
            return True
        return False

    # Método de representação
    def __str__(self) -> str:
        """ Representação de string do Contato (para exibição na Agenda).
        Exemplo: "Nome :: [Celular] 9999-9999, [Casa] 8888-8888" """
        # Junta a representação de string de todos os fones.
        fones_str = ", ".join(str(f) for f in self._fones)
        return f"{self._nome} :: {fones_str}"
