from models.Funcionario import Funcionario
from models.Endereco import Endereco
from models.enums.Sexo import Sexo
from models.enums.Setor import Setor

class Motoboy(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo, matricula: str, setor:Setor, salario: float, cnh:str) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo, matricula, setor, salario)
        self.cnh = cnh

    def salario_final(self)->float:
        return f"Salário Final: {self.salario}"

    def __str__(self) -> str:
        return (f"Motoboy:\n"
                f"Nome: {self.nome}\n"
                f"Telefone: {self.telefone}\n"
                f"Email: {self.email}\n"
                f"CPF: {self.cpf}\n"
                f"RG: {self.rg}\n"
                f"Data de Nascimento: {self.dataNascimento}\n"
                f"Sexo: {self.sexo.texto}\n"
                f"Matrícula: {self.matricula}\n"
                f"Setor: {self.setor}\n"
                f"Salário: {self.salario}\n"
                f"CNH: {self.cnh}\n"
                f"Endereço: {self.endereco}\n"
                f"\n\n{self.salario_final()}"
                )
        