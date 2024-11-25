from models.Fisica import Fisica
from models.Endereco import Endereco
from models.enums.Sexo import Sexo

class Cliente(Fisica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo, protocoloAtendimento:int) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo)
        self.protocoloAtendimento = protocoloAtendimento

    def __str__(self) -> str:
        return (
            f"Cliente"
            f"\n Nome: {self.nome}"
            f"\n Telefone: {self.telefone}"
            f"\n Email: {self.email}"
            f"\n Cpf: {self.cpf}"
            f"\n Rg: {self.rg}"
            f"\n Data de Nascimento: {self.dataNascimento}"
            f"\n Sexo: {self.sexo.texto}"
            f"\n Protocolo de Atendimento: {self.protocoloAtendimento}"
            f"\n {self.endereco}"
        )    