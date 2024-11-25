from enum import Enum

class Setor(Enum):
    ENGENHARIA = "Engenharia"
    SAUDE = "Saúde"
    JURIDICO = "Juridico"
    OPECAOES = "Operações"

    def __init__(self, nome:str) -> None:
        self.nome = nome
        