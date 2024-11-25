from models.Pessoa import Pessoa
from models.Endereco import Endereco

class Juridica(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cnpj:str, inscricaoEstadual:str) -> None:
            super().__init__(nome, telefone, email, endereco)
            self.cnpj = cnpj
            self.inscricaoEstadual = inscricaoEstadual
    
    
    def __str__(self) -> str:
          return (
                  f"Juridica: "
                  f"\nNome: {self.nome}"
                  f"\nTelefone: {self.telefone}"
                  f"\nEmail: {self.email}"
                  f"\nCnpj: {self.cnpj}"
                  f"\nInscrição Estadual: {self.inscricaoEstadual}"
                  f"\n{self.endereco}"
                  )
              
