from os import system
from models.Motoboy import Motoboy
from models.Medico import Medico
from models.Advogado import Advogado
from models.Endereco import Endereco
from models.enums.Sexo import Sexo
from models.enums.Setor import Setor
from models.enums.UnidadeFederativa import UnidadeFederativa
from models.Cliente import Cliente
from models.Juridica import Juridica
system("cls||clear")

endereco_medico = Endereco("Rua BEIA", "130", "1º Andar", "40711 - 600", "Salvador", UnidadeFederativa.BAHIA.nome)
endereco_motoboy = Endereco("Avenida Paulista", "1000", "Apartamento 202", "01310-100", "São Paulo", UnidadeFederativa.SAO_PAULO.nome)
endereco_advogado = Endereco("Rua do Comércio", "500", "Sala 101", "20010-000", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO.nome)
endereco_cliente = Endereco("Rua das Palmeiras", "45", "Bloco B", "20250-400", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO.nome)
endereco_juridica = Endereco("Avenida das Nações", "1000", "Conjunto 501", "22222-000", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO.nome)



medico = Medico("Douglas","71 98472 - 9798","douglas.a.silva7@ba.estudante.senai.br",endereco_medico, "06358631231", "1223131231", "25/03/2007", Sexo.MASCULINO, "1231231313123", Setor.ENGENHARIA, 2532.00, "12312")

motoboy = Motoboy("Carlos Souza","11 98765-4321","carlos.souza@entrega.com",endereco_motoboy,"98765432100","345678912","15/07/1990",Sexo.MASCULINO,"202056",Setor.OPECAOES,1800.00,"1234567890")

advogado = Advogado("Fernanda Oliveira","61 99876-5432","fernanda.oliveira@advocacia.com",endereco_advogado,"12345678901","987654321","23/05/1985",Sexo.FEMININO,"305762",Setor.JURIDICO,4500.00,"DF123456")

cliente = Cliente("Ana Costa","21 99999-8888","ana.costa@exemplo.com",endereco_cliente,"98765432100","321654987","10/11/1992",Sexo.FEMININO,"AT202309001")

juridica = Juridica("Empresa Exemplo LTDA","21 98888-7777","contato@empresaexemplo.com",endereco_juridica,"12.345.678/0001-90","12345678")

print(medico)
print("\n")
print(cliente)
print("\n")
print(motoboy)
print("\n")
print(advogado)
print("\n")
print(juridica)