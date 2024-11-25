from models.enums.UnidadeFederativa import UnidadeFederativa

class Endereco:
    def __init__(self, logradouro:str, numero:str, complemento:str, cep:str, cidade:str, uf:UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf

    def __str__(self) -> str:
        return (
            f"\nEndereço: "
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\nCidade: {self.cidade}"
            f"\nUnidade Federativa: {self.uf}"
        )
    