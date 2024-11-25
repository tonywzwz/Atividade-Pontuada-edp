from abc import ABC, abstractmethod
from models.Pessoa import Pessoa
from models.enums.Sexo import Sexo
from models.Endereco import Endereco

class Fisica(Pessoa, ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf:str, rg:str, dataNascimento:str, sexo:Sexo) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf
        self.rg = rg
        self.dataNascimento = dataNascimento
        self.sexo = sexo

    