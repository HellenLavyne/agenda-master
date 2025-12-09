from src.identificador import Identificador


class Fone:
    # Caracteres permitidos em um número de telefone (dígitos, parênteses, hífen, ponto).
    CARACTERES_VALIDOS = "0123456789()-."

    def __init__(self, identificador: Identificador, numero: str):

        self._identificador = identificador
        self._numero = numero

    @staticmethod
    def validarNumero(numero) -> bool:
        if not numero:
            return False

        # O número só deve conter caracteres da lista CARACTERES_VALIDOS.
        return all(c in Fone.CARACTERES_VALIDOS for c in numero)

    def getIdentificador(self) -> Identificador:
        # Retorna o Identificador do fone.
        return self._identificador

    def getNumero(self) -> str:
        # Retorna o número de telefone.
        return self._numero

    # Métodos de Representação e Comparação
    def __str__(self) -> str:
        return f"[{self.getIdentificador()}] {self.getNumero()}"

    def __repr__(self) -> str:
        return f"Fone(identificador={self.getIdentificador()}, numero='{self.getNumero()}')"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Fone):
            # Compara usando os Getters para consistência
            return self.getIdentificador() == other.getIdentificador() and self.getNumero() == other.getNumero()
        return NotImplemented
