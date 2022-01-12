from .Connection import postgree
from pydantic import BaseModel


class Endereco(BaseModel):
    endereco_id: int
    rua: str
    complemento: str
    bairro: str
    cidade: str
    estado: str
    cep: str


def insertEndereco(endereco: Endereco):
    conn = postgree()
    print(f'insert \'endereco\' {endereco}')
    response = conn.mutation(
        f'INSERT INTO ENDERECO (ENDERECO_ID, RUA, COMPLEMENTO, BAIRRO, CIDADE, ESTADO, CEP) values ({endereco.endereco_id}, \'{endereco.rua}\', \'{endereco.complemento}\', \'{endereco.bairro}\', \'{endereco.cidade}\', \'{endereco.estado}\', \'{endereco.cep}\');')


def listEnderecos():
    conn = postgree()
    enderecos = conn.query("""SELECT * FROM ENDERECO;""")
    print(f'list all \'endereco\'')
    return enderecos


def updateEndereco(endereco: Endereco):
    conn = postgree()
    print(f'update \'endereco\' {endereco} ')
    return conn.mutation(
        f'UPDATE ENDERECO SET RUA = \'{endereco.rua}\', COMPLEMENTO = \'{endereco.complemento}\', BAIRRO = \'{endereco.bairro}\', CIDADE = \'{endereco.cidade}\', ESTADO = \'{endereco.estado}\', CEP = \'{endereco.cep}\' WHERE ENDERECO_ID = \'{endereco.endereco_id}\';')


def deleteEndereco(endereco_id: int):
    conn = postgree()
    print(f'delete \'endereco\' from id {endereco_id}')
    response = conn.mutation('DELETE FROM ENDERECO e WHERE e.ENDERECO_ID = endereco_id;')
    return response
