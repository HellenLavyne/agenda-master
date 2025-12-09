
from src.contato import Contato
from src.identificador import Identificador
from src.fone import Fone
from typing import List, Optional, Dict


class Agenda:

    def __init__(self):
        """ Inicializa a agenda com um dicionário para armazenar os contatos.
        A chave é o nome do contato em minúsculas."""

        self._contatos: Dict[str, Contato] = {}

    def getContatos(self) -> list[Contato]:
        """ Retorna a lista de todos os contatos, ordenada alfabeticamente pelo nome."""
        # Ordena a lista de objetos Contato pelo atributo 'nome'.
        return sorted(self._contatos.values(), key=lambda c: c.getName())

    def getQuantidadeDeContatos(self) ->  int:
        # Retorna o número total de contatos cadastrados.
        return len(self._contatos)

    def getContato(self, nome:str) -> Contato:
        #Busca um contato pelo nome.
        return self._contatos.get(nome.lower())

    def adicionarContato(self, contato: Contato) -> bool:
        # Adiciona um novo Contato ou mescla fones em um Contato existente.
        nome_key = contato.getName().lower()

        # Não deve ser possível adicionar um contato sem telefone.
        if contato.getQuantidadeFones() == 0:
            return False

        if nome_key in self._contatos:
            # Se o contato já existe, mesma os fones do novo contato
            contato_existente = self._contatos[nome_key]
            for fone in contato.getFones():
                contato_existente.adicionarFone(fone)
            return False
        else:
            # Adicionar o novo contato
            self._contatos[nome_key] = contato
            return True

    def removerContato(self, nome: str) -> bool:
        # Remove um contato pelo nome
        nome_key = nome.lower()
        if nome_key in self._contatos:
            del self._contatos[nome_key]
            return True
        return False

    def removerFone(self, nome:str, index: int) -> bool:
        # Remove um telefone de um contato pelo índice.
        contato = self.getContato(nome)
        if contato:
            # Chama o método de remoção na classe Contato
            return contato.removerFone(index)
        return False

    def getQuantidadeDeFonesPorIdentificador(self, identificador: Identificador) -> int:
        # Retorna a quantidade total de fones de um Identificador específico.
        total = 0
        for contato in self._contatos.values():
            for fone in contato.getFones():
                if fone.getIdentificador() == identificador:
                    total += 1
        return total

    def getQuantidadeTotalDeFones(self) -> int:
        # Retorna a quantidade total de fones cadastrados em toda a agenda.
        total = 0
        for contato in self._contatos.values():
            total += contato.getQuantidadeFones()
        return total

    def pesquisar(self, expressao:str) -> list[Contato]:
        # Busca contatos por uma expressão em todos os campos: nome, identificador e número do fone.
        expressao_lower = expressao.lower()
        contatos_encontrados: List[Contato] =  []

        for contato in self._contatos.values():
            # Busca no nome do contato
            if expressao_lower in contato.getName().lower():
                contatos_encontrados.append(contato)
                continue

            # Busca nos fones do contato
            for fone in contato.getFones():

                # Busca no identificador
                if expressao_lower in fone.getIdentificador().identificador.lower():
                    contatos_encontrados.append(contato)
                    break # Encontrou um fone, pode parar de checar os fones.

                # Busca no número
                if expressao_lower in fone.getNumero():
                    contatos_encontrados.append(contato)
                    break # Encontrou um fone, pode parar de checar os fones.

        return sorted(contatos_encontrados, key=lambda c: c.getName())

    def __str__(self) -> str:
        # Retorna a representação de string de toda a agenda.
        output = ["--- Agenda ---"]
        contatos_ordenados = self.getContatos() # Lista de contatos ordenados
        for contato in contatos_ordenados:
            output.append(str(contato))

        # Adiciona o resumo da agenda
        output.append("--- Resumo ---")
        output.append(f"Contatos: {self.getQuantidadeDeContatos()}")
        output.append(f"Fones (Total): {self.getQuantidadeTotalDeFones()}")

        # Conta a quantidade por identificador
        for identificador in Identificador:
            count = self.getQuantidadeDeFonesPorIdentificador(identificador)
            output.append(f"Fones({identificador.identificador}): {count}")

        return "\n".join(output)